/**
 * @file   gpio_test.c
 * @author Derek Molloy
 * @date   8 November 2015
 * @brief  A kernel module for controlling a GPIO LED/button pair. The
 * device mounts an LED and pushbutton via sysfs /sys/class/gpio/gpio60
 * and gpio46 respectively. */

#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/gpio.h>                 // for the GPIO functions
#include <linux/interrupt.h>            // for the IRQ code

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Derek Molloy");
MODULE_DESCRIPTION("A Button/LED test driver for the Beagle");
MODULE_VERSION("0.1");

static unsigned int gpioRedLED = 44;       // P9_12/P2.8 (GPIO60)
static unsigned int gpioRedButton = 46;    // P8_16/P2.22 (GPIO46)
static unsigned int gpioBlueLED = 45;       // P9_12/P2.8 (GPIO60)
static unsigned int gpioBlueButton = 47;    // P8_16/P2.22 (GPIO46)
static unsigned int irqNumberRed, irqNumberBlue;          // share IRQ num within file
static unsigned int numberPresses = 0;  // store number of presses
static bool	    ledOn = 0;          // used to invert state of LED

unsigned int LEDArray[] ={44, 23}; //array of LEDs
unsigned int ButtonArray[] ={46, 47}; //array of buttons

int i; //variable for for loops

// prototype for the custom IRQ handler function, function below
static irq_handler_t  ebb_gpio_irq_handler(unsigned int irq, void
                                    *dev_id, struct pt_regs *regs);

/** @brief The LKM initialization function */
static int __init ebb_gpio_init(void){
   int resultRed = 0;
   int resultBlue = 0;
   printk(KERN_INFO "GPIO_TEST: Initializing the GPIO_TEST LKM\n");
   if (!gpio_is_valid(gpioRedLED)){
      printk(KERN_INFO "GPIO_TEST: invalid LED GPIO\n");
      return -ENODEV;
   }
   for(i = 0; i<2; i++){
      gpio_request(LEDArray[i], "sysfs");          // request LED GPIO
      gpio_direction_output(LEDArray[i], ledOn);   // set in output mode and on
      gpio_set_value(LEDArray[i], 0);          // not required
      gpio_export(LEDArray[i], false);             // appears in /sys/class/gpio
   			               // false prevents direction change
      gpio_request(ButtonArray[i], "sysfs");       // set up gpioButton
      gpio_direction_input(ButtonArray[i]);        // set up as input
      gpio_set_debounce(ButtonArray[i], 200);      // debounce delay of 200ms
      gpio_export(ButtonArray[i], false);          // appears in /sys/class/gpio
   }

   printk(KERN_INFO "GPIO_TEST: red button value is currently: %d, and the blue button value is currently: %d\n",
          gpio_get_value(gpioRedButton), gpio_get_value(gpioBlueButton));
   irqNumberRed = gpio_to_irq(gpioRedButton);     // map GPIO to IRQ number
   irqNumberBlue = gpio_to_irq(gpioBlueButton);     // map GPIO to IRQ number
   printk(KERN_INFO "GPIO_TEST: red button mapped to IRQ: %d, and blue button mapped to IRQ: %d\n", irqNumberRed, irqNumberBlue);

   // This next call requests an interrupt line
   resultRed = request_irq(irqNumberRed,         // interrupt number requested
            (irq_handler_t) ebb_gpio_irq_handler, // handler function
            IRQF_TRIGGER_RISING | IRQF_TRIGGER_FALLING,  // on rising edge (press, not release)
            "ebb_gpio_handler",  // used in /proc/interrupts
            NULL);                // *dev_id for shared interrupt lines
   resultBlue = request_irq(irqNumberBlue,         // interrupt number requested
            (irq_handler_t) ebb_gpio_irq_handler, // handler function
            IRQF_TRIGGER_RISING | IRQF_TRIGGER_FALLING,  // on rising edge (press, not release)
            "ebb_gpio_handler",  // used in /proc/interrupts
            NULL);
   printk(KERN_INFO "GPIO_TEST: IRQ request result (red) is: %d and IRQ request result (blue) is: %d\n", resultRed, resultBlue);
   return resultRed;
}

/** @brief The LKM cleanup function  */
static void __exit ebb_gpio_exit(void){
   printk(KERN_INFO "GPIO_TEST: red button value is currently: %d, and ble button value is currently: %d\n",
          gpio_get_value(gpioRedButton), gpio_get_value(gpioBlueButton));
   printk(KERN_INFO "GPIO_TEST: pressed %d times\n", numberPresses);
   for(i = 0; i<2; i++){
      gpio_set_value(LEDArray[i], 0);    // turn the red LED off
      gpio_unexport(LEDArray[i]);        // unexport the LED GPIO
      // free_irq(irqNumberRed, NULL);     // free the IRQ number, no *dev_id
      gpio_unexport(ButtonArray[i]);     // unexport the Button GPIO
      gpio_free(LEDArray[i]);            // free the LED GPIO
      gpio_free(ButtonArray[i]);         // free the Button GPIO
      printk(KERN_INFO "GPIO_TEST: Goodbye from the LKM!\n");
   }
   free_irq(irqNumberRed, NULL);     // free the IRQ number, no *dev_id
   free_irq(irqNumberBlue, NULL);     // free the IRQ number, no *dev_id
}

/** @brief The GPIO IRQ Handler function
 * A custom interrupt handler that is attached to the GPIO. The same
 * interrupt handler cannot be invoked concurrently as the line is
 * masked out until the function is complete. This function is static
 * as it should not be invoked directly from outside of this file.
 * @param irq    the IRQ number associated with the GPIO
 * @param dev_id the *dev_id that is provided - used to identify
 * which device caused the interrupt. Not used here.
 * @param regs   h/w specific register values -used for debugging.
 * return returns IRQ_HANDLED if successful - return IRQ_NONE otherwise.
 */
static irq_handler_t ebb_gpio_irq_handler(unsigned int irq,
                        void *dev_id, struct pt_regs *regs){
   gpio_set_value(gpioRedLED,  gpio_get_value(gpioRedButton));     // set LED accordingly
   gpio_set_value(gpioBlueLED,  gpio_get_value(gpioBlueButton));     // set LED accordingly
   printk(KERN_INFO "GPIO_TEST: Interrupt! red button has value %d, and blue button has value %d\n",
          gpio_get_value(gpioRedButton), gpio_get_value(gpioBlueButton));
   numberPresses++;                    // global counter
   return (irq_handler_t) IRQ_HANDLED; // announce IRQ handled
}

module_init(ebb_gpio_init);
module_exit(ebb_gpio_exit);
