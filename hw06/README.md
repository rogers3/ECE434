Author: Christina Rogers (rogersc@rose-hulman.edu)

CM: 473

Date: 10/5/2020

What is included:

| Name      | Description |
| ----------- | ----------- |
|  ResponseTimeNoLoad.JPG | Picture of Cyclic test with no load.
|  ResponseTimeWithLoad.JPG | Picture of Cyclic test with a heavy load.

## Project: ##
I added some project ideas to the Project page and marked the ones I am intrested in

## Watch: ##
Answers to questions:
1.  National Instruments
2.	The PREEMPT RT patch makes Linux into a real time system. Its goal is to increase the predictability and reduce the latencies of the kernel directly modifying the existent kernel code
3.	Mixed criticality is when you have tasks with different degrees of time sensitivities. For example, if you are going to run tasks with real time requirements as well as non-time critical tasks.
4.	Drivers may schedule non-RT tasks before RT tasks. This is because driver stacks are shared between tasks in preempt_rt.
5.	Delta – The time it takes from the occurrence of an external event to the relevant real-time task execution.
6.	Takes a time stamp and sleeps for a fixed duration and then take another time stamp when that thread is woken up. Delta is the difference between the two-time stamps.
7.	Histogram that depicts the difference in delta (see question 5) between preempt and preempt_rt (cyclictest). Preempt has a max bound of 342 microseconds whereas preempt_rt has a max bound of 16 microseconds. This makes preempt_rt more well behaved for tasks with real-time requirements.
8.	Dispatch latency is the amount of time it takes between the hardware firing and the relevant thread to be woken up. Scheduling latency is the time it takes from once the scheduler is made aware of a high priority task to the CPU being given the task.
9.	In the mainline model there are long running interrupts which are a cause for dispatch latency. One reason for long running interrupts is that interrupt cannot be handled until all previous interrupts are done executing. So, a critical interrupt must wait for previous interrupts to execute even if they are non-critical.
10.	An interrupt must wait for previous interrupts to execute before it can be handled. In this figure there is a non-critical interrupt before the external event. So, the external event must wait for the non-critical interrupt to execute before starting.
11.	The external event can start sooner in figure 4 because with the RT patch, IRQ threads are forced. This means there is only a little code that is executed in the heart interrupt context. This code just wakes up the associated handle thread that executes the IRQ handler. Since running in threads, threads can be preempted.

## PREEMPT_RT: ##

No Load:

![alt text](https://github.com/rogers3/ECE434/blob/master/hw06/ResponseTimeNoLoad.JPG)


With Load:

![alt text](https://github.com/rogers3/ECE434/blob/master/hw06/ResponseTimeWithLoad.JPG)


Comment:

The RT kernel does have shorter and bounded latency which apperears to be around 100 microseconds. I loaded the kernels by compiling a make file and then cleaning it repeatedly to make tasks.
