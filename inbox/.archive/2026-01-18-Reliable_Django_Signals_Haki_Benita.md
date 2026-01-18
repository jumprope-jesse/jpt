---
type: link
source: notion
url: https://hakibenita.com/django-reliable-signals
notion_type: Software Repo
tags: ['Running']
created: 2025-10-30T18:14:00.000Z
---

# Reliable Django Signals | Haki Benita

## Overview (from Notion)
- The article offers insights into improving reliability in Django applications, a topic that resonates with your role as a software engineer and founder.
- Emphasizes the importance of decoupling modules, which could inspire you to streamline processes within your own company.
- The use of signals for communication in software parallels the communication skills needed in parenting and leadership; fostering collaboration is key in both areas.
- Highlights the balance between maintaining system performance and ensuring reliability, a challenge you likely face in managing work-life balance.
- The implementation of background tasks can be seen as a metaphor for delegating responsibilities at home and work, emphasizing the importance of teamwork.
- Considers the potential pitfalls of overcomplicating systems, prompting a reflection on simplicity in both software design and family life.
- Offers a fresh perspective on handling failures, suggesting that the right approach can turn setbacks into opportunities for growth, whether in software or personal challenges.
- Challenges traditional views on signal handling, inviting you to think creatively about problem-solving in your business ventures.

## AI Summary (from Notion)
Django signals can be unreliable due to their underlying transport, but an alternative implementation using background tasks can enhance their reliability for critical workflows. The article discusses creating a payment process with Django, managing order statuses based on payment outcomes, and addresses challenges like circular dependencies. It introduces a new tasks framework in Django for executing signals reliably, ensuring that changes to database objects and task execution occur atomically, thus preventing inconsistent states. The implementation also highlights the importance of decoupling modules while maintaining functionality and reliability in workflows.

## Content (from Notion)

Django signals are extremely useful for decoupling modules and implementing complicated workflows. However, the underlying transport for signals makes them unreliable and subject to unexpected failures.

In this article, I present an alternative transport implementation for Django signals using background tasks which makes them reliable and safer to use in mission critical workflows.

Say you have an application that accept payments from users. Usually, you don't go and implement your own payment solution. Instead, you integrate with some 3rd-party provider.

### Creating a Payment Process

This is a common workflow for integrating with a 3rd-party payment provider:

1. You create some payment process in the provider's system
1. You redirect the user to some URL, or you get something to pass to the provider's client SDK
1. Sometime in the future you get notified about the status of the payment, usually by webhook or redirect
A simple state machine for a payment process can look like this:

payment process state machine

To keep track of payments you create a simple Django module:

```plain text
# payment/models.py

from typing import Literal, Self
from django.db import models, transaction


class Error(Exception):
    # Abstract.
    pass

class StateError(Error):
    pass


class PaymentProcess(models.Model):
    id = models.BigAutoField(primary_key=True)
    amount = models.BigIntegerField()
    status: Literal['initiated', 'succeeded', 'failed'] = models.CharField(max_length=20)

    @classmethod
    def create(cls, *, amount: int) -> Self:
        assert amount > 0
        return cls.objects.create(amount=amount, status='initiated')

    @classmethod
    def set_status(cls, id: int, *, succeeded: bool) -> Self:
        with transaction.atomic():
            payment_process = cls.objects.select_for_update(of=('self', ), no_key=True).get(id=id)
            if payment_process.status not in {'initiated'}:
                raise StateError()
            if succeeded:
                payment_process.status = 'succeeded'
            else:
                payment_process.status = 'failed'
            payment_process.save()

        return payment_process

```

To create a new payment process you provide an amount:

```plain text
>>> from payment.models import PaymentProcess
>>> pp = PaymentProcess.create(amount=100_00)
>>> print(vars(pp))
{'id': 1, 'amount': 10000, 'status': 'initiated'}

```

The initial status is "initiated". At some point you'll make an API call to your payment provider, get some ID and pass it over to the client - this is outside the scope of this article.

Next, the user interacts with the 3rd-party to provide their payment details. When the user is done, you get an update on the outcome of the payment, usually a webhook or a redirect, and you set the status of the payment process in your local database:

```plain text
>>> pp = PaymentProcess.set_status(1, succeeded=True)
>>> print(vars(pp))
{'id': 1, 'amount': 10000, 'status': 'succeeded'}

```

The payment succeeded and the status is set to "succeeded". So far so good!

Now that you can process payment, you can move on to handling orders.

In your website, the user browse around until they find something they want, and proceed to checkout. At this point, you calculate the amount to be paid and create an order with a payment process. The user then interacts with the payment process to complete the payment. Based on the outcome of the payment, you decide if the order should be filled or cancelled.

A state machine for an order can look like this:

order state machine

To keep track of orders you create a new "orders" module:

```plain text
from django.db import models, transaction
from payment.models import PaymentProcess
from typing import Literal, Self

class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    payment_process = models.ForeignKey(PaymentProcess, on_delete=models.PROTECT)
    amount = models.BigIntegerField()
    status: Literal['pending_payment', 'completed', 'cancelled'] = models.CharField(max_length=20)

    @classmethod
    def create(cls, *, amount: int) -> Self:
        assert amount > 0
        with transaction.atomic():
            payment_process = PaymentProcess.create(amount=amount)
            order = cls.objects.create(
                payment_process=payment_process,
                amount=amount,
                status='pending_payment',
            )
        return order

```

To create the order you provide an amount to charge. The module then goes and create a payment process for the same amount and associates it with your order via a foreign key:

```plain text
>>> o = Order.create(amount=120_00)
>>> print(vars(o))
{ 'id': 1, 'payment_process_id': 2, 'amount': 12000, 'status': 'pending_payment'}
>>> print(vars(o.payment_process))
{ 'id': 2, 'amount': 12000, 'status': 'initiated'}

```

In real life, when you create an order you keep a lot more information such as the user who placed the order, the items, shipping information and so on. All of this is not important for this article, so we ignore it.

The initial state of an order is "pending_payment" and the current state of the payment is "initiated". The next step is for the user to complete the payment.

When a payment is updated, we need to update the state of the order. Here is a function that given a payment process, sets the status of the order:

```plain text
# order/models.py
class Order(models.Model):
    # ...

    @classmethod
    def on_payment_completed(cls, *, payment_process_id: int) -> Self:
        """Update the order status based on the payment process status."""
        with transaction.atomic():
            order = (
                cls.objects
                .select_related('payment_process')
                .select_for_update(of=('self', ), no_key=True)
                .get(payment_process_id=payment_process_id)
            )
            if order.status not in {'pending_payment'}:
                return order

            match order.payment_process.status:
                case 'succeeded':
                    order.status = 'completed'
                case 'failed':
                    order.status = 'cancelled'
                case 'initiated':
                    assert False, f'Unexpected payment process status "{order.payment_process.status}"'
                case ever:
                    assert_never(ever)

            order.save()

        return order

```

The function first looks for the order that references the payment process. If the status of the order is not "pending_payment", we assume this function was already called, and we return the order. This provides some level of idempotency. In real life, you probably should verify that the current state of the order matches the state of the provided payment process.

Next, update the status of the order based on the status of the payment process, save to the database, and return the updated order.

This is where it gets hairy...

Who's in charge of calling this function? The order is not aware of changes to the payment process, so what's triggering this function?

When you create an order, the order creates a payment process. The order module is referencing the payment module using a foreign key, therefore, the order module depends on the payment module:

module dependencies

In our workflow, after the user completes the payment, the payment module receives a webhook with the outcome of the payment, and the status of the payment process is updated. Our order is not aware of changes to the payment process, so at what point do we trigger a change in the order?

A naive way of doing this is to simply update the order directly from the payment process using the reverse relation:

```plain text
diff --git i/payment/models.py w/payment/models.py
 from typing import Literal, Self
 from django.db import models, transaction
+from order.models import Order

@@ -13,23 +13,25 @@  class PaymentProcess(models.Model):
     @classmethod
     def set_status(cls, id: int, *, succeeded: bool) -> Self:
         with transaction.atomic():
             payment_process = cls.objects.select_for_update(of=('self', ), no_key=True).get(id=id)
             if payment_process.status not in {'initiated'}:
                 raise StateError()
             if succeeded:
                 payment_process.status = 'succeeded'
             else:
                 payment_process.status = 'failed'
             payment_process.save()

+            Order.on_payment_completed(payment_process_id=payment_process.id)

         return payment_process

```

Now, when the payment process is updated, it explicitly goes to the order and attempts to update it as well. However, if you try to execute this, you'll get an exception:

```plain text
$./manage.py check
Traceback (most recent call last):
    ... snipped ...
ImportError: cannot import name 'PaymentProcess' from partially initialized
module 'payment.models' (most likely due to a circular import) (payment/models.py)

```

Python is warning us about a circular dependency! An order currently references a payment process. With this change, the payment process is referencing the order back - this creates a circular dependency:

circular dependency

There is a way to make this work - you can import the order inside the function - but you should really avoid that. A circular dependency is usually a symptom of bad design!

Another reason this is a bad approach is that payment process is a low level module - it can potentially be used by other modules other than order. Should a low level module like payment be aware of all the modules that are using it? This won't scale well and will cause a web of dependencies within the application.

To avoid circular dependency we can't have the payment process reference the order directly. Another approach, is for the order to periodically check for changes in relevant payment process:

```plain text
from django.core.management.base import BaseCommand
from ...models import Order

class Command(BaseCommand):
    help = 'Check all orders with pending payment and update their status if needed.'

    def handle(self, *args, **options):
        for payment_process_id in Order.objects.filter(
            status='pending_payment',
            payment_process__status__in=['succeeded', 'failed'],
        ).values_list('payment_process_id', flat=True):
            order = Order.on_payment_completed(payment_process_id=payment_process_id)
            self.stdout.write(self.style.SUCCESS(f'order {order.id} status changed to "{order.status}"'))

```

This Django management command is looking for orders pending payment with a payment process that reached either "failed" or "succeeded" state, and triggers a status update for the order.

To demonstrate, create an order and mark the payment as successful:

```plain text
>>> o = Order.create(amount=120_00)
>>> o.payment_process_id
3
>>> pp = PaymentProcess.set_status(3, succeeded=True)
>>> print(vars(pp))
{ 'id': 2, 'payment_process_id': 3, 'amount': 12000, 'status': 'pending_payment'}
>>> o.refresh_from_db()
>>> print(vars(o))
{ 'id': 3, 'amount': 12000, 'status': 'initiated'}

```

Notice that the payment completed successfully, but the order is pending payment. Let's use the management command to sync the state:

```plain text
$ ./manage.py sync_orders_pending_payment
order 2 status changed to "completed"

```

Great! You can now execute this task on a schedule and your orders will eventually reach the correct state.

This approach has several advantages and disadvantages:

- 
- 
- 
- 
- 
Using scheduled tasks is a good and reliable solution. However, for user-facing workflows that require quick response it's often not a good fit.

So far we tried to trigger a change in the order from the payment it references. This caused circular dependencies so we decided it's a bad idea. We then tried polling for changes which proved to be reliable and simple, but introduced unacceptable delays in the workflow.

To address these challenges, Django provides signals dispatcher as a way to communicate between modules in the system:

> 

Using signals dispatcher, we can dispatch a signal and have one or more receivers subscribe to it. In our case, the payment process can send a signal when it completes, and the order can subscribe to it and update its status. Using signals the payment module can communicate with other modules in the system without explicitly depending on them!

decouple modules using signals

First, define the signal:

```plain text
# payment/signals.py.
from django.dispatch import Signal

payment_process_completed = Signal()

```

Next, send the signal when the payment completes:

```plain text
diff --git i/payment/models.py w/payment/models.py
 from typing import Literal, Self
 from django.db import models, transaction

+from . import signals

@@ -13,23 +15,28 @@ class PaymentProcess(models.Model):
     @classmethod
     def set_status(cls, id: int, *, succeeded: bool) -> Self:
         with transaction.atomic():
             payment_process = cls.objects.select_for_update(of=('self', ), no_key=True).get(id=id)
             if payment_process.status not in {'initiated'}:
                 raise StateError()
             if succeeded:
                 payment_process.status = 'succeeded'
             else:
                 payment_process.status = 'failed'
             payment_process.save()

+            signals.payment_process_completed.send(
+                sender=None,
+                payment_process_id=payment_process.id,
+            )
+
         return payment_process

```

The order can now register a receiver that will be executed when the "payment_process_completed" signal is sent. This requires some minor adjustments on the receiving end:

```plain text
diff --git a/order/models.py b/order/models.py
+from __future__ import annotations
 from django.db import models, transaction
 from payment.models import PaymentProcess
 from typing import Literal, Self, assert_never
+from django.dispatch import receiver

+import payment.signals

@@ -21,16 +24,22 @@ class Order(models.Model):
-    @classmethod
-    def on_payment_completed(cls, *, payment_process_id: int) -> Self:
+    @staticmethod
+    @receiver(payment.signals.payment_process_completed, dispatch_uid='1da6190f-0cf1-45e1-8481-0d1e27bf6e6f')
+    def on_payment_completed(payment_process_id: int, *args, **kwargs) -> Order | None:
         """Update the order status based on the payment process status."""
         with transaction.atomic():
-            order = (
-                cls.objects
-                .select_related('payment_process')
-                .select_for_update(of=('self', ), no_key=True)
-                .get(payment_process_id=payment_process_id)
-            )
+            try:
+                order = (
+                    Order.objects
+                    .select_related('payment_process')
+                    .select_for_update(of=('self', ), no_key=True)
+                    .get(payment_process_id=payment_process_id)
+                )
+            except Order.DoesNotExist:
+                # Not related to order.
+                return None
+
             if order.status not in {'pending_payment'}:
                 return order

```

Let's break it down:

- 
- 
- 
- 
- 
- 
We can now see it in action:

```plain text
>>> o = Order.create(amount=150_00)
>>> print(vars(o))
{'id': 3, 'payment_process_id': 4, 'amount': 15000, 'status': 'pending_payment'}
>>> PaymentProcess.set_status(4, succeeded=True)
>>> o.refresh_from_db()
>>> print(vars(o))
{'id': 3, 'payment_process_id': 4, 'amount': 15000, 'status': 'completed'}

```

Notice how the state of the order changes to "completed" even though we did not explicitly call Order.on_payment_completed. This function was invoked implicitly when PaymentProcess.set_status dispatched the signal.

Using signals we can trigger changes in other modules without creating direct dependencies between them. As the documentation promised, signals allow us to keep modules decoupled. In our scenario, using signals, payment processes can trigger changes in orders without explicitly depending on them - problem solved!

This principle of keeping modules decoupled should also extend to how we name signals. It's tempting to name our signal something like "complete_order", but that creates an implicit dependency between the modules because this name implies intent - the payment process should not be aware of how its signal is being used. Instead, we name signals in a way that only reflects what happened, in our case "payment completed". Each receiver can then make whatever they want from that!

Another advantage of signals is that they can have many receivers. If for example we have an "analytics" module and we want to keep track of how many payment processes succeeded or failed, we can simply register another receiver for the same signal and increment some counter.

In the next sections we are going to challenge the signals approach and demonstrate when it falls short of its promise!

In the previous section we used signals as a way to communicate between two modules without creating an explicit dependency between them. But, did we really achieve that?

Consider what happens when a receiver encounters an error and raises an exception:

```plain text
>>> o = Order.create(amount=160_00)
>>> PaymentProcess.set_status(o.payment_process_id, succeeded=True)
---------------------------------------------------------------------------
Exception                                 Traceback (most recent call last)
Cell In[2], line 1
----> 1 PaymentProcess.set_status(o.payment_process_id, succeeded=True)

File payment/models.py:37, in PaymentProcess.set_status(cls, id, succeeded)
File .venv/lib/python3.13/site-packages/django/dispatch/dispatcher.py:209, in Signal.send(self, sender, **named)
File order/models.py:31, in Order.on_payment_completed(payment_process_id, *args, **kwargs)
     27 @staticmethod
     28 @receiver(payment.signals.payment_process_completed, dispatch_uid='1da6190f-0cf1-45e1-8481-0d1e27bf6e6f')
     29 def on_payment_completed(payment_process_id: int, *args, **kwargs) -> Order | None:
     30     """Update the order status based on the payment process status."""
---> 31     raise Exception("on_payment_completed FAILED!!")
     32     with transaction.atomic():
     33         try:

Exception: on_payment_completed FAILED!!

```

Oh no! An error in the order caused the payment process to fail. We thought payment process has nothing to do with orders any more, but we were wrong! To keep modules truly decoupled we can't have exceptions from signal receivers propagate to the signal sender.

Django provides another way of sending a signal, in a way that does not propagate errors to the sender:

```plain text
--- a/payment/models.py
+++ b/payment/models.py
@@ -34,7 +34,7 @@ class PaymentProcess(models.Model):
                 payment_process.status = 'failed'
             payment_process.save()

-            signals.payment_process_completed.send(
+            signals.payment_process_completed.send_robust(
                 sender=None,
                 payment_process_id=payment_process.id,
             )

```

The documentation for Signal.send_robust explain the difference very well:

> 

Using send_robust() we can make sure that our modules remain decoupled even when errors happen.

So, are we finally truly decoupled?

### Django Signals and Database Transactions

In the previous section we found that we weren't decoupled as we thought when the receiver raises an exception. We switched from Signal.send to Signal.send_robust which doesn't propagate errors. So now we are no longer affected by anything the receiver is doing, right? Not really!

Imagine we have another module, "analytics", to keep track of metrics in our system. To keep count of how many successful and failed payment processes we set up this simple receiver:

```plain text
# analytics/handlers.py
import urllib.request
from django.dispatch import receiver

import payment.models import PaymentProcess
import payment.signals

@receiver(payment.signals.payment_process_completed, dispatch_uid='a4e3cd9c-1314-40c1-8251-955c20dd5d93')
def on_payment_process_completed(payment_process_id: int, *args, **kwargs) -> None:
    status = PaymentProcess.objects.values_list('status', flat=True).get(id=payment_process_id)
    response = urllib.request.urlopen('https://myanalytics.com/metric/inc', data={'key': 'payment_process:{status}'})
    if response.status != 200:
        raise Exception('Failed to increase metric')

```

The function fetches the status of the payment process and reports to some 3rd-party analytics service. We already know that if this fails the sender will not be affected. But what will happen if this request takes a very long time?

Receiver functions are called immediately by the signals framework when the signal is sent. This means where and when we send the signal is significant. This is where we send the payment_completed signal:

```plain text
class PaymentProcess(models.Model):
    # ...
    @classmethod
    def set_status(cls, id: int, *, succeeded: bool) -> Self:
        with transaction.atomic():
            payment_process = cls.objects.select_for_update(of=('self', ), no_key=True).get(id=id)
            if payment_process.status not in {'initiated'}:
                raise StateError()
            if succeeded:
                payment_process.status = 'succeeded'
            else:
                payment_process.status = 'failed'
            payment_process.save()

            signals.payment_process_completed.send_robust(
                sender=None,
                payment_process_id=payment_process.id,
            )

        return payment_process

```

The signal is sent inside a database transaction. This can cause some problems:

- 
- 
- 
The most straight forward solution here is to simply send the signal outside of the transaction:

```plain text
--- a/payment/models.py
@@ -15,28 +15,28 @@ class PaymentProcess(models.Model):
     @classmethod
     def set_status(cls, id: int, *, succeeded: bool) -> Self:
         with transaction.atomic():
             payment_process = cls.objects.select_for_update(of=('self', ), no_key=True).get(id=id)
             if payment_process.status not in {'initiated'}:
                 raise StateError()
             if succeeded:
                 payment_process.status = 'succeeded'
             else:
                 payment_process.status = 'failed'
             payment_process.save()

-            signals.payment_process_completed.send_robust(
-                sender=None,
-                payment_process_id=payment_process.id,
-            )
+        signals.payment_process_completed.send_robust(
+            sender=None,
+            payment_process_id=payment_process.id,
+        )

         return payment_process

```

Sending the signal outside of the database transaction prevents prolonged transactions and issues that can be caused by unexpected side-effects, however, the solution is still not 100% reliable!

Django provides a nice way of executing something only after the database transaction completed successfully, without having to move the call down. Using on_commit we can trust that the signal is only being sent after the transaction was successfully committed. If the transaction rolls-back, the callable in on_commit will not be executed, and the signal will not be sent.

To understand how reliable our approach really is, we need to evaluate what happens when it fails at different points in the process. The easiest way of thinking about it is to imagine the server crashing while your process is running.

Consider the following places where the server might crash during the execution of the function:

```plain text
@classmethod
def set_status(cls, id: int, *, succeeded: bool) -> Self:
    # 💥 Before the transaction
    with transaction.atomic():
        payment_process = cls.objects.select_for_update(of=('self', ), no_key=True).get(id=id)
        if payment_process.status not in {'initiated'}:
            raise StateError()
        if succeeded:
            payment_process.status = 'succeeded'
        else:
            payment_process.status = 'failed'

        payment_process.save()
        # 💥 Inside the transaction

    # 💥 After the transaction, before the signal is sent

    signals.payment_process_completed.send_robust(
        sender=None,
        payment_process_id=payment_process.id,
    )

    return payment_process

```

Let's analyze what happens if the server crashes in each of these points:

- 
- 
- 
Our approach is not resilient to server crash at any point in the process so we have to consider it unreliable!

Database transactions provide atomicity - changes to multiple rows inside a single transaction are commited all at once or not at all. Ideally, we want the change to the payment and the following change to the order to be executed "all or nothing", otherwise, we risk leaving the process in an inconsistent state.

In our case, the change to the order is triggered by the signal which is sent outside the database transaction so we cannot guarantee atomic execution of both these changes. As a result, if the payment is updated and we crash before we sent the signal, the system will charge the user but the order will never be marked as completed! You'll end up with very angry users, and for a good reason.

We started by using Django signals to decouple modules. We then refined our implementation to minimize the impact of receivers on callers by sending signals outside the database transaction. As a result, we introduced scenarios that can leave the process in an inconsistent state.

Despite our best efforts so far, we are still left with a few significant problems:

- 
- 
- 
All of these problems are not new, but they are rooted in the way Django signals work. An ideal solution should provide the following guarantees:

- Receivers should be executed at-least-once if the sender committed
- Receivers should not execute if the sender's transaction rolled back (due to failure or otherwise)
- Receivers should have minimal effect on the sender
A lot of work and careful thought went into the Django signals framework, and the API is actually quite nice! So with that in mind, we'll try to adjust the execution mechanism for Django signals so that it's reliable and compatible as possible with the existing framework.

Django 6.0 introduces a new "Tasks Framework":

> 

Django tasks in its initial release is mostly an interface - it comes with two built-in backends, dummy and immediate, which are mostly intended for debug and development. The idea behind this approach is that developers can implement their own backends, and have seamless integration with other applications using Django tasks.

One prominent backend that has been developed in parallel with the tasks framework is the DatabaseBackend of django-tasks. The database backend maintains a queue in a database table, and provides a worker implementation to dequeue and execute tasks. It also comes with a built-in retry mechanism and a nice admin panel.

Using a database queue we can make changes to database objects and enqueue tasks atomically.

This is the idea:

- We send a signal in the database transaction of the sender.
- When a signal is sent, we enqueue a task in the database queue for each receiver.
- The receiver tasks are not visible to workers until the sender transaction is commited.
- Once the sender transaction commits, worker processes can start executing receiver tasks.
- If the sender transaction rollback, the enqueued receiver tasks are also rolled-back and therefor won't execute.
- If a receiver happens to fail, the worker can retry it.
- Depending on the number of workers, we can execute multiple receiver tasks at the same time, minimizing delays in the overall workflow.
This approach checks all of our requirements!

First, since we're using the new tasks framework and the database backend, we need to install Django version 6 and django-tasks:

```plain text
$ uv add "Django>=6"
$ uv add django-tasks

```

Next, configure django-tasks and set the default backend to be the DatabaseBackend:

```plain text
+++ settings.py
@@ -38,6 +38,8 @@ INSTALLED_APPS = [
     'order.apps.OrderConfig',
     'payment.apps.PaymentConfig',
+    'django_tasks',
+    'django_tasks.backends.database',
 ]

@@ -117,3 +119,10 @@ USE_TZ = True
+
+TASKS = {
+    "default": {
+        "BACKEND": "django_tasks.backends.database.DatabaseBackend",
+        "ENQUEUE_ON_COMMIT": False,
+    }
+}

```

Make sure you are using a PostgreSQL database backend:

```plain text
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangoreliablesignals',
        'USER': 'djangoreliablesignals',
    }
}

```

Run the migrations to create the queue tables:

```plain text
$ ./manage.py migrate

```

Tasks are executed by a worker process. This means in addition to the processes that run Django itself, you also need a worker process running in the background. In another shell:

```plain text
$ ./manage.py db_worker

```

Make sure to check the options for the worker if this ever makes it to production!

Great, on to the actual implementation...

### Execute Receivers as Django Tasks

A Django signal is essentially a registry of receiver functions. When you use the receiver decorator, the wrapped function is added to a list of receivers on the signal instance. When you send the signal, the signal is iterating over the internal list of receivers and executes them.

One of the limitations of a database queue is that to enqueue a task, you must save all of the necessary information for executing it to the database. This means you need to serialize all the information to JSON - this includes the arguments as well.

In our case, to execute a receiver function we need to be able to tell the worker what function to execute. Since we can't persist a function object to the database, we need to find another way of referencing it. One way to reference a function is to generate a string with the name of the module and the fully qualified name of the function:

```plain text
from typing import Callable, Any

def callable_to_qualname(f: Callable[..., Any]) -> str:
    """Return the <module>::<qualname> identifier of a function."""
    return f'{f.__module__}::{f.__qualname__}'

```

The function produces a string that includes the module name and the fully qualified name of the function we want to reference:

```plain text
>>> callable_to_qualname(Order.on_payment_completed)
'order.models::Order.on_payment_completed'

```

To get the function from the string, we implement the opposite function:

```plain text
import importlib

def qualname_to_callable(qualname: str) -> Callable[..., Any]:
    """Get a callable from its <module>::<qualname> identifier."""
    module_name, func_qualname = qualname.split('::', 1)
    module = importlib.import_module(module_name)

    # Handle nested attributes (e.g., 'ClassName.method_name')
    obj = module
    for attr in func_qualname.split('.'):
        obj = getattr(obj, attr)

    return obj  # type: ignore[return-value]

```

Given the fully qualified name we generated, the function returns the callable:

```plain text
>>> receiver = qualname_to_callable('order.models::Order.on_payment_completed')
>>> receiver
<function order.models.Order.on_payment_completed(payment_process_id: 'int', *args, **kwargs) -> 'Order | None'>

```

Now that we are able to persist a reference to our receiver function, we can create a task to execute an arbitrary receiver:

```plain text
from collections.abc import Mapping
from django_tasks import task

@task()
def execute_task_signal_receiver(
    *,
    receiver_qualname: str,
    named: Mapping[str, object],
) -> None:
    receiver = qualname_to_callable(receiver_qualname)
    receiver(signal=None, sender=None, **named)

```

This registers a new django-tasks task that accepts a receiver qualified name and arguments, and executes it. Simple as that!

To change the way signals are sent, we provide an alternative implementation of a Django Signal that instead of executing receivers immediately, enqueues a task for each one:

```plain text
# reliable_signal/__init__.py
from django.dispatch import Signal as DjangoSignal
from django.dispatch.dispatcher import NO_RECEIVERS

class Signal(DjangoSignal):
    """A django-workers-capable signal."""

    def send_reliable(self, sender: None, **named) -> None:
        """Like send_robust(), but enqueues a task for each registered receiver."""
        if not self.receivers:
            return
        if self.sender_receivers_cache.get(sender) is NO_RECEIVERS:
            return
        sync_receivers, async_receivers = self._live_receivers(sender)
        assert not async_receivers, 'Async receivers not supported by task'
        for receiver in sync_receivers:
            execute_task_signal_receiver.enqueue(
                receiver_qualname=callable_to_qualname(receiver),
                named=named,
            )

```

Our reliable signal is extending Django's built-in Signal class and adds a function called send_reliable. The function works like send_robust, but instead of executing the receiver functions immediately, it enqueues a task for each receiver instead. We discuss this approach further later on.

Finally, to adjust our code to use the reliable signal, all we need to do is to use our new reliable signal, and replace send_robust with send_reliable:

```plain text
diff --git i/payment/signals.py w/payment/signals.py
@@ -1,3 +1,3 @@
-from django.dispatch import Signal
+from reliable_signal import Signal

 payment_process_completed = Signal()

diff --git i/payment/models.py w/payment/models.py
@@ -34,9 +34,9 @@ class PaymentProcess(models.Model):
                 payment_process.status = 'failed'
             payment_process.save()

-        signals.payment_process_completed.send_robust(
-            sender=None,
-            payment_process_id=payment_process.id,
-        )
+            signals.payment_process_completed.send_reliable(
+                sender=None,
+                payment_process_id=payment_process.id,
+            )

         return payment_process

```

Notice that we enqueue the task inside the database transaction. Previously, we said this might cause some issues, but using a database queue, you actually do want to enqueue the task inside the sender transaction. This way, the task will be executed only after the sender commits. If the sender rollback, the task will not be enqueued and will not be executed.

Now we are ready to test this out. Make sure you have a worker running and execute this in Django shell:

```plain text
>>> o = Order.create(amount=170_00)
>>> PaymentProcess.set_status(o.payment_process_id, succeeded=True)
<PaymentProcess: PaymentProcess object (7)>
>>> o.refresh_from_db()
>>> o.status
'completed'

```

Amazing! Quickly after we set the status for payment process, the worker picked up the task and updated the status of the order. You can see it in the worker logs as well:

```plain text
$ ./manage.py db_worker
Watching for file changes with StatReloader
Starting worker worker_id=4tLA6TEzAdIZ7W620DrVnHuC342wiDfs queues=default
Task id=c34fa024-db4d-41b4-b875-723b2436a346 path=reliable_signal.execute_task_signal_receiver_simple state=RUNNING
Task id=c34fa024-db4d-41b4-b875-723b2436a346 path=reliable_signal.execute_task_signal_receiver_simple state=SUCCEEDED

```

We now have a reliable execution engine for Django signals:

- Receivers are enqueued inside the sender database transaction
- Failed receivers can be retried by the tasks framework
- Enqueuing receivers is quick, with minimal impact on sender function
When we test workflows we usually don't care much about the execution engine, but rather with the business logic. We also want to keep our test suite simple and deterministic as possible - this means we don't want to execute receivers in another worker, we want to execute them immediately.

If you recall, we mentioned that Django comes with two built-in backends for testing and development. One of them is the ImmediateBackend. This backend will execute tasks immediately when they are enqueued - exactly what we need in tests.

```plain text
from django.test import TestCase, override_settings
from order.models import Order
from payment.models import PaymentProcess

@override_settings(TASKS={'default': {'BACKEND': 'django.tasks.backends.immediate.ImmediateBackend'}})
class OrderTestCase(TestCase):
    def test_order_happy_path(self):
        order = Order.create(amount=100_00)
        self.assertEqual(order.status, 'pending_payment')
        self.assertEqual(order.amount, 100_00)
        self.assertEqual(order.payment_process.status, 'initiated')
        self.assertEqual(order.payment_process.amount, 100_00)

        # This will trigger the signal, which should execute the receiver immediately
        PaymentProcess.set_status(order.payment_process_id, succeeded=True)
        order.refresh_from_db()
        self.assertEqual(order.status, 'completed')
        self.assertEqual(order.payment_process.status, 'succeeded')

```

This tests the common "happy path" for an order - create an order, payment is successful, order status is updated. To provide an alternative backend for tasks during the test, we use the @override_settings with the path to the built-in ImmediateBackend.

Running the test:

```plain text
$ ./manage.py test
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.058s

OK
Destroying test database for alias 'default'...

```

Great! We now have reliable execution that we can easily test.

Reliable signals provide great benefits, but they also come with some restrictions and limitations:

- 
- 
- 
Due to these limitations, we think it is crucial that reliable signals co-exist with the built-in signal system:

- Reliable signals don't fit all types of signals so we don't attempt to monkey-patch Django. Instead, reliable signals should be explicitly defined using reliable_signal.Signal.
- Due to the different behavior, offloading execution to a background task should be explicitly invoked using send_reliable rather than attempting to patch send_robust or send.
The current implementation is mostly offered as a reference. While operational under the restrictions mentioned above, there are a few bits we did not address:

- 
- 
- 
- 
We have a lot of custom workflow in our systems - this is really most of what we do! We are using Django signals extensively in situations where two decoupled modules needs to communicate with each other. As our system grew, we experienced first-hand the issues that can come from having un-reliable signals. Eventually, we developed our own database task queue and integrated it with Django signals. So far its been working pretty well with moderate traffic.

This article was motivated by our pains and learning from implementing reliable signals in our systems. The release of the the Django tasks framework (and the backends) is surely a welcome addition to an increasing number of large systems built with Django, that needs to have reliable and durable workflows.


