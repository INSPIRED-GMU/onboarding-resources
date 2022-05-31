#### Table of contents

- [Introduction](#introduction)
  - [2.x now in maintenance mode](#2x-now-in-maintenance-mode)
  - [Maven coordinates](#maven-coordinates)
  - [Java 8](#java-8)
  - [Package structure](#package-structure)
- [Behavior changes](#behavior-changes)
  - [More undeliverable errors](#more-undeliverable-errors)
  - [Connectable source reset](#connectable-source-reset)
  - [Flowable.publish pause](#flowablepublish-pause)
  - [Processor.offer null-check](#processoroffer-null-check)
  - [MulticastProcessor.offer fusion-check](#multicastprocessoroffer-fusion-check)
  - [Group abandonment in groupBy](#group-abandonment-in-groupby)
  - [Backpressure in groupBy](#backpressure-in-groupby)
  - [Window abandonment in window](#window-abandonment-in-window)
  - [CompositeException cause generation](#compositeexception-cause-generation)
  - [Parameter validation exception change](#parameter-validation-exception-change)
  - [From-callbacks upfront cancellation](#from-callbacks-upfront-cancellation)
  - [Using cleanup order](#using-cleanup-order)
- [API changes](#api-changes)
  - [Functional interfaces](#functional-interfaces)
  - [New Types](#new-types)
  - [Moved components](#moved-components)
  - [API promotions](#api-promotions)
  - [API additions](#api-additions)
  - [Java 8 additions](#java-8-additions)
  - [API renames](#api-renames)
  - [API signature changes](#api-signature-changes)
  - [API removals](#api-removals)
- [Interoperation](#interoperation)
  - [RxJava 1.x](#rxjava-1x)
  - [RxJava 2.x](#rxjava-2x)
  - [Java 9](#java-9)
  - [Swing](#swing)
  - [Project Loom](#project-loom)
- [Miscellaneous](#miscellaneous)

# Introduction

Welcome to the new major release of RxJava, a library for composing asynchronous and event-based programs using observable sequences for the Java VM.

As with every such release, there have been quite a lot of trivial and non-trivial changes, cleanups and improvements all across the codebase, which warrant some detailed and comprehensive explanations nonetheless.

With each major release, we take the liberty to introduce potential and actual binary and behavioral incompatible changes so that past mistakes can be corrected and technical debt can be repaid.

Please read this guide to its full extent before posting any issue about "why X no longer compiles". Please also take note of sentences marked with :warning: indicating some migration pitfalls. Information about related discussions and the code changes themselves can be found in each section under the :information_source: **Further references:** marker.

## 2.x now in maintenance mode

With the release of RxJava 3.0.0, the previous version line, 2.2.x, is in maintenance mode. This means **only bugfixes** will be accepted and applied; **no new operators** or **documentation changes** will be accepted or applied.

:information_source: 2.x will be supported until **February 28, 2021**, after which all development on that branch will stop.

## Maven coordinates

RxJava 3 lives in the group [`io.reactivex.rxjava3`](https://search.maven.org/search?q=io.reactivex.rxjava3) with artifact ID [`rxjava`](https://search.maven.org/artifact/io.reactivex.rxjava3/rxjava). Official language/platform adaptors will also be located under the group [`io.reactivex.rxjava3`](https://search.maven.org/search?q=io.reactivex.rxjava3).

The following examples demonstrate the typical import statements. Please consider the latest version and replace `3.0.0` with the numbers from the badge: [![Maven Central](https://maven-badges.herokuapp.com/maven-central/io.reactivex.rxjava3/rxjava/badge.svg)](https://maven-badges.herokuapp.com/maven-central/io.reactivex.rxjava3/rxjava)

### Gradle import

```groovy
dependencies {
  implementation 'io.reactivex.rxjava3:rxjava:3.0.0'
}
```

### Maven import

```xml
<dependency>
  <groupId>io.reactivex.rxjava3</groupId>
  <artifactId>rxjava</artifactId>
  <version>3.0.0</version>
</dependency>
```

:information_source: **Further references:** PR [#6421](https://github.com/ReactiveX/RxJava/pull/6421)

## JavaDocs

The 3.x documentation of the various components can be found at 

- http://reactivex.io/RxJava/3.x/javadoc/

Sub-version specific documentation is available under a version tag, for example

- http://reactivex.io/RxJava/3.x/javadoc/3.0.0-RC9

(replace `3.0.0-RC9` with the numbers from the badge: [![Maven Central](https://maven-badges.herokuapp.com/maven-central/io.reactivex.rxjava3/rxjava/badge.svg)](https://maven-badges.herokuapp.com/maven-central/io.reactivex.rxjava3/rxjava)).

The documentation of the current snapshot is under

- http://reactivex.io/RxJava/3.x/javadoc/snapshot


## Java 8

For a long time, RxJava was limited to Java 6 API due to how Android was lagging behind in its runtime support. This changed with the upcoming Android Studio 4 previews where a process called [desugaring](https://developer.android.com/studio/preview/features#j8-desugar) is able to turn many Java 7 and 8 features into Java 6 compatible ones transparently. 

This allowed us to increase the baseline of RxJava to Java 8 and add official support for many Java 8 constructs:

- `Stream`: use `java.util.stream.Stream` as a source or expose sequences as **blocking** `Stream`s.
- Stream `Collector`s: aggregate items into collections specified by [standard transformations](https://docs.oracle.com/javase/8/docs/api/java/util/stream/Collector.html).
- `Optional`: helps with the **non-null**ness requirement of RxJava
- `CompletableFuture`: consume `CompletableFuture`s non-blockingly or expose single results as `CompletableFuture`s.
- Use site non-null annotation: helps with some functional types be able to return null in specific circumstances.

However, some features won't be supported:

- `java.time.Duration`: would add a lot of overloads; can always be decomposed into the `time` + `unit` manually.
- `java.util.function`: these can't throw `Throwable`s, overloads would create bloat and/or ambiguity

Consequently, one has to change the project's compilation target settings to Java 8:

```groovy
sourceCompatibility = JavaVersion.VERSION_1_8
targetCompatibility = JavaVersion.VERSION_1_8
```

or

```groovy
android {
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
}
```

<a name="#desugar"><a href="#desugar">⚠️</a> **Note on the internal Java 8 support**

Due to the state of the Android Desugar tooling, as of writing this page, the internals of pre-existing, non-Java 8 related RxJava operators do not use Java 8 constructs or types. This allows using these "older" operators with Android API levels where the desugaring tool doesn't provide automatic Java 8 backports of various constructs.

:information_source: **Further references:** Issue [#6695](https://github.com/ReactiveX/RxJava/issues/6695), PR [#6765](https://github.com/ReactiveX/RxJava/pull/6765), [other PRs](https://github.com/ReactiveX/RxJava/pulls?utf8=%E2%9C%93&q=label%3A%22Java+8%22+)

## Package structure

RxJava 3 components are located under the `io.reactivex.rxjava3` package (RxJava 1 has `rx` and RxJava 2 is just `io.reactivex`. This allows version 3 to live side by side with the earlier versions. In addition, the core types of RxJava (`Flowable`, `Observer`, etc.) have been moved to `io.reactivex.rxjava3.core`.

Component | RxJava 2 | RxJava 3 |
----------|---------|----------|
Core | `io.reactivex` | `io.reactivex.rxjava3.core` |
Annotations | `io.reactivex.annotations` | `io.reactivex.rxjava3.annotations` |
Disposables | `io.reactivex.disposables` | `io.reactivex.rxjava3.disposables` |
Exceptions| `io.reactivex.exceptions` | `io.reactivex.rxjava3.exceptions` |
Functions | `io.reactivex.functions` | `io.reactivex.rxjava3.functions` |
Flowables | `io.reactivex.flowables` | `io.reactivex.rxjava3.flowables` |
Observables | `io.reactivex.observables` | `io.reactivex.rxjava3.observables` |
Subjects | `io.reactivex.subjects` | `io.reactivex.rxjava3.subjects` |
Processors | `io.reactivex.processors` | `io.reactivex.rxjava3.processors` |
Observers | `io.reactivex.observers` | `io.reactivex.rxjava3.observers` |
Subscribers | `io.reactivex.subscribers` | `io.reactivex.rxjava3.subscribers` |
Parallel | `io.reactivex.parallel` | `io.reactivex.rxjava3.parallel` |
Internal| `io.reactivex.internal` | `io.reactivex.rxjava3.internal` |

<a name="#organizeimports"><a href="#organizeimports">⚠️</a> **Note on running "Organize Imports" from the IDE**

Due to naming matches, IDE's tend to import `java.util.Observable` instead of picking RxJava's `io.reactivex.rxjava3.core.Observable`. One can usually have the IDE ignore `java.util.Observable` and `java.util.Observer`, or otherwise, specify an explicit `import io.reactivex.rxjava3.core.Observable;` in the affected files.

Also since RxJava 3 now requires a Java 8 runtime, the standard library functional interfaces, such as `java.util.function.Function`, may be picked instead of `io.reactivex.rxjava3.functions.Function`. IDEs tend to give non-descriptive errors such as "Function can't be converted to Function", omitting the fact about the package differences.

:information_source: **Further references:** PR [#6621](https://github.com/ReactiveX/RxJava/pull/6621)

# Behavior changes

Sometimes, the design of components and operators turn out to be inadequate, too limited or wrong in some circumstances. Major releases such as this allow us to make the necessary changes that would have caused all sorts of problems in a patch release.

## More undeliverable errors

With RxJava 2.x, [the goal was set](https://github.com/ReactiveX/RxJava/wiki/What's-different-in-2.0#error-handling) to not let any errors slip away in case the sequence is no longer able to deliver them to the consumers for some reason. Despite our best efforts, errors still could have been lost in various race conditions across many dozen operators.

Fixing this in a 2.x patch would have caused too much trouble, therefore, the fix was postponed to the, otherwise already considerably changing, 3.x release. Now, canceling an operator that delays errors internally will signal those errors to the global error handler via `RxJavaPlugins.onError()`.

### undeliverable-example

```java
RxJavaPlugins.setErrorHandler(error -> System.out.println(error));

PublishProcessor<Integer> main = PublishProcessor.create();
PublishProcessor<Integer> inner = PublishProcessor.create();

// switchMapDelayError will delay all errors
TestSubscriber<Integer> ts = main.switchMapDelayError(v -> inner).test();

main.onNext(1);

// the inner fails
inner.onError(new IOException());

// the consumer is still clueless
ts.assertEmpty();

// the consumer cancels
ts.cancel();

// console prints 
// io.reactivex.rxjava3.exceptions.UndeliverableException: 
// The exception could not be delivered to the consumer because 
// it has already canceled/disposed the flow or the exception has 
// nowhere to  go to begin with. Further reading: 
// https://github.com/ReactiveX/RxJava/wiki/What's-different-in-2.0#error-handling 
// | java.io.IOException
```


:information_source: **Further references:** [PRs](https://github.com/ReactiveX/RxJava/pulls?utf8=%E2%9C%93&q=is%3Apr+undeliverable+is%3Aclosed+label%3A3.x)

## Connectable source reset

The purpose of the connectable types (`ConnectableFlowable` and `ConnectableObservable`) is to allow one or more consumers to be prepared before the actual upstream gets streamed to them upon calling `connect()`. This worked correctly for the first time, but had some trouble if the upstream terminated instead of getting disconnected. In this terminating case, depending on whether the connectable was created with `replay()` or `publish()`, fresh consumers would either be unable to receive items from a new connection or would miss items altogether.

With 3.x, connectables have to be reset explicitly when they terminate. This extra step allows consumers to receive cached items or be prepared for a fresh connection.

### publish-reset example

With `publish`, if the connectable terminates, consumers subscribing later will only receive the terminal event. One has to call `reset()` so that a late consumer will receive items from a fresh connection.

```java
ConnectableFlowable<Integer> connectable = Flowable.range(1, 10).publish();

// prepare consumers, nothing is signaled yet
connectable.subscribe(/* ... */);
connectable.subscribe(/* ... */);

// connect, current consumers will receive items
connectable.connect();

// let it terminate
Thread.sleep(2000);

// late consumers now will receive a terminal event
connectable.subscribe(
    item -> { }, 
    error -> { }, 
    () -> System.out.println("Done!"));

// reset the connectable to appear fresh again
connectable.reset();

// fresh consumers, they will also be ready to receive
connectable.subscribe(
    System.out::println, 
    error -> { }, 
    () -> System.out.println("Done!")
);

// connect, the fresh consumer now gets the new items
connectable.connect();
```
### replay-reset example

With `replay`, if the connectable terminates, consumers subscribing later will receive the cached items. One has to call `reset` to discard this cache so that late consumers can then receive fresh items.

```java
ConnectableFlowable<Integer> connectable = Flowable.range(1, 10).replay();

// prepare consumers, nothing is signaled yet
connectable.subscribe(System.out::println);
connectable.subscribe(System.out::println);

// connect, current consumers will receive items
connectable.connect();

// let it terminate
Thread.sleep(2000);

// late consumers will still receive the cached items
connectable.subscribe(
    System.out::println, 
    error -> { }, 
    () -> System.out.println("Done!"));

// reset the connectable to appear fresh again
connectable.reset();

// fresh consumers, they will also be ready to receive
connectable.subscribe(
    System.out::println, 
    error -> { }, 
    () -> System.out.println("Done!")
);

// connect, the fresh consumer now gets the new items
connectable.connect();
```

:information_source: **Further references:** Issue [#5628](https://github.com/ReactiveX/RxJava/issues/5628), PR [#6519](https://github.com/ReactiveX/RxJava/pull/6519)

## Flowable.publish pause

The implementation of `Flowable.publish` hosts an internal queue to support backpressure from its downstream. In 2.x, this queue, and consequently the upstream source, was slowly draining on its own if all of the resulting `ConnectableFlowable`'s consumers have cancelled. This caused unexpected item loss when the lack of consumers was only temporary.

With 3.x, the implementation pauses and items already in the internal queue will be immediately available to consumers subscribing a bit later.

### publish-pause example

```java
ConnectableFlowable<Integer> connectable = Flowable.range(1, 200).publish();

connectable.connect();

// the first consumer takes only 50 items and cancels
connectable.take(50).test().assertValueCount(50);

// with 3.x, the remaining items will be still available
connectable.test().assertValueCount(150);
```

:information_source: **Further references:** Issue [#5899](https://github.com/ReactiveX/RxJava/issues/5628), PR [#6519](https://github.com/ReactiveX/RxJava/pull/6519)

## Processor.offer null-check

Calling `PublishProcessor.offer()`, `BehaviorProcessor.offer()` or `MulticastProcessor.offer` with a null argument now throws a `NullPointerException` instead of signaling it via `onError` and thus terminating the processor. This now matches the behavior of the `onNext` method required by the [Reactive Streams specification](https://github.com/reactive-streams/reactive-streams-jvm#2.13).

### offer-example

```java
PublishProcessor<Integer> pp = PublishProcessor.create();

TestSubscriber<Integer> ts = pp.test();

try {
   pp.offer(null);
} catch (NullPointerException expected) {
}

// no error received
ts.assertEmpty();

pp.offer(1);

// consumers are still there to receive proper items
ts.asssertValuesOnly(1);
```

:information_source: **Further references:** PR [#6799](https://github.com/ReactiveX/RxJava/pull/6799)

## MulticastProcessor.offer fusion-check

`MulticastProcessor` was designed to be processor that coordinates backpressure like the `Flowable.publish` operators do. It includes internal optimizations such as operator-fusion when subscribing it to the right kind of source.

Since users can retain the reference to the processor itself, they could, in concept, call the `onXXX` methods and possibly cause trouble. The same is true for the `offer` method which, when called while the aforementioned fusion is taking place, leads to undefined behavior in 2.x.

With 3.x, the `offer` method will throw an `IllegalStateException` and not disturb the internal state of the processor.

:information_source: **Further references:** PR [#6799](https://github.com/ReactiveX/RxJava/pull/6799)

## Group abandonment in groupBy

The `groupBy` operator is one of the peculiar operators that signals reactive sources as its main output where consumers are expected to subscribe to these inner sources as well. Consequently, if the main sequence gets cancelled (i.e., the `Flowable<GroupedFlowable<T>>` itself), the consumers should still keep receiving items on their groups but no new groups should be created. The original source can then only be cancelled if all of such inner consumers have cancelled as well.

However, in 2.x, nothing is forcing the consumption of the inner sources and thus groups may be simply ignored altogether, preventing the cancellation of the original source and possibly leading to resource leaks.

With 3.x, the behavior of `groupBy` has been changed so that when it emits a group, the downstream has to subscribe to it synchronously. Otherwise, the group is considered "abandoned" and terminated. This way, abandoned groups won't prevent the cancellation of the original source. If a late consumer still subscribes to the group, the item that triggered the group creation will be still available.

Synchronous subscription means the following flow setups **will cause abandonment** and possibly group re-creation:

### groupBy abandonment example

```java
// observeOn creates a time gap between group emission
// and subscription
source.groupBy(v -> v)
.observeOn(Schedulers.computation())
.flatMap(g -> g)

// subscribeOn creates a time gap too
source.groupBy(v -> v)
.flatMap(g -> g.subscribeOn(Schedulers.computation()))
```

Since the groups are essentially hot sources, one should use `observeOn` to move the processing of the items safely to another thread anyway:

```java
source.groupBy(v -> v)
.flatMap(g -> 
    g.observeOn(Schedulers.computation())
    .map(v -> v + 1)
)
```

:information_source: **Further references:** Issue [#6596](https://github.com/ReactiveX/RxJava/pull/6596), PR [#6642](https://github.com/ReactiveX/RxJava/pull/6642)

## Backpressure in groupBy

The `Flowable.groupBy` operator is even more peculiar in a way that it has to coordinate backpressure from the consumers of its inner group and request from its original `Flowable`. The complication is, such requests can lead to a creation of a new group, a new item for the group that itself requested or a new item for a completely different group altogether. Therefore, groups can affect each other's ability to receive items and can hang the sequence, especially if some groups don't get to be consumed at all.

This latter can happen when groups are merged via `flatMap` where the number of individual groups is greater than the `flatMap`'s concurrency level (defaul 128) so fresh groups won't get subscribed to and old ones may not complete to make room. With `concatMap`, the same issue can manifest immediately.

Since RxJava is non-blocking, such silent hangs are difficult to detect and diagnose (i.e., no thread is blocking in `groupBy` or `flatMap`). Therefore, 3.x changed the behavior of `groupBy` so that if the immediate downstream is unable to receive a new group, the sequence terminates with `MissingBackpressureException`:

### groupBy backpressure example

```java
Flowable.range(1, 1000)
.groupBy(v -> v)
.flatMap(v -> v, 16)
.test()
.assertError(MissingBackpressureException);
```

The error message will also indicate the group index:

> Unable to emit a new group (#16) due to lack of requests. Please make sure the downstream can always accept a new group and each group is consumed for the whole operator to be able to proceed.
 
Increasing the concurrency level to the right amount (or `Integer.MAX_VALUE` if the number of groups is not known upfront) should resolve the problem:

```java
.flatMap(v -> v, 1000)
```

:information_source: **Further references:** Issue [#6641](https://github.com/ReactiveX/RxJava/pull/6641), PR [#6740](https://github.com/ReactiveX/RxJava/pull/6740)

## Window abandonment in window

Similar to [groupBy](#group-abandonment-in-groupby), the `window` operator emits inner reactive sequences that should still keep receiving items when the outer sequence is cancelled (i.e., working with only a limited set of windows). Similarly, when all window consumers cancel, the original source should be cancelled as well.

However, in 2.x, nothing is forcing the consumption of the inner sources and thus windows may be simply ignored altogether, preventing the cancellation of the original source and possibly leading to resource leaks.

With 3.x, the behavior of all `window` operators has been changed so that when it emits a group, the downstream has to subscribe to it synchronously. Otherwise, the window is considered "abandoned" and terminated. This way, abandoned windows won't prevent the cancellation of the original source. If a late consumer still subscribes to the window, the item that triggered the window creation *may be* still available.

Synchronous subscription means the following flow setups **will cause abandonment**:

### window abandonment example

```java
// observeOn creates a time gap between window emission
// and subscription
source.window(10, 5)
.observeOn(Schedulers.computation())
.flatMap(g -> g)

// subscribeOn creates a time gap too
source.window(1, TimeUnit.SECONDS)
.flatMap(g -> g.subscribeOn(Schedulers.computation()))
```

Since the windows are essentially hot sources, one should use `observeOn` to move the processing of the items safely to another thread anyway:

```java
source.window(1, TimeUnit.SECONDS)
.flatMap(g -> 
    g.observeOn(Schedulers.computation())
    .map(v -> v + 1)
)
```

:information_source: **Further references:** PR [#6758](https://github.com/ReactiveX/RxJava/pull/6758), PR [#6761](https://github.com/ReactiveX/RxJava/pull/6761), PR [#6762](https://github.com/ReactiveX/RxJava/pull/6762)

## CompositeException cause generation

In 1.x and 2.x, calling the `CompositeException.getCause()` method resulted in a generation of a chain of exceptions from the internal list of aggregated exceptions. This was mainly done because Java 6 lacks the suppressed exception feature of Java 7+ exceptions. However, the implementation was possibly mutating exceptions or, sometimes, unable to establish a chain at all. Given the source of the original contribution of the method, it was risky to fix the issues with it in 2.x.

With 3.x, the method constructs a cause exception that when asked for a stacktrace, generates an output without touching the aggregated exceptions (which is IDE friendly and should be navigable):

### stacktrace example

```
Multiple exceptions (2)
|-- io.reactivex.rxjava3.exceptions.TestException: ex3
    at io.reactivex.rxjava3.exceptions.CompositeExceptionTest.nestedMultilineMessage(CompositeExceptionTest.java:341)
|-- io.reactivex.rxjava3.exceptions.TestException: ex4
    at io.reactivex.rxjava3.exceptions.CompositeExceptionTest.nestedMultilineMessage(CompositeExceptionTest.java:342)
  |-- io.reactivex.rxjava3.exceptions.CompositeException: 2 exceptions occurred. 
      at io.reactivex.rxjava3.exceptions.CompositeExceptionTest.nestedMultilineMessage(CompositeExceptionTest.java:337)
    |-- io.reactivex.rxjava3.exceptions.CompositeException.ExceptionOverview: 
        Multiple exceptions (2)
        |-- io.reactivex.rxjava3.exceptions.TestException: ex1
            at io.reactivex.rxjava3.exceptions.CompositeExceptionTest.nestedMultilineMessage(CompositeExceptionTest.java:335)
        |-- io.reactivex.rxjava3.exceptions.TestException: ex2
            at io.reactivex.rxjava3.exceptions.CompositeExceptionTest.nestedMultilineMessage(CompositeExceptionTest.java:336)
```

![image](https://user-images.githubusercontent.com/1269832/70315342-a9308600-1819-11ea-81d2-b56694dbd9e8.png)

:information_source: **Further references:** Issue [#6747](https://github.com/ReactiveX/RxJava/pull/6747), PR [#6748](https://github.com/ReactiveX/RxJava/pull/6748)

## Parameter validation exception change

Some standard operators in 2.x throw `IndexOutOfBoundsException` when the respective argument was invalid. For consistency with other parameter validation exceptions, the following operators now throw `IllegalArgumentException` instead:

- `skip`
- `skipLast`
- `takeLast`
- `takeLastTimed`

:information_source: **Further references:** PR [#6831](https://github.com/ReactiveX/RxJava/pull/6831), PR [#6835](https://github.com/ReactiveX/RxJava/pull/6835)

## From-callbacks upfront cancellation

In 2.x, canceling sequences created via `fromRunnable` and `fromAction` were inconsistent with other `fromX` sequences when the downstream cancelled/disposed the sequence immediately.

In 3.x, such upfront cancellation will not execute the given callback.

### from callback example

```java
Runnable run = mock(Runnable.class);

Completable.fromRunnable(run)
.test(true); // cancel upfront

verify(run, never()).run();
```

:information_source: **Further references:** PR [#6873](https://github.com/ReactiveX/RxJava/pull/6873)

## Using cleanup order

The operator `using` has an `eager` parameter to determine when the resource should be cleaned up: `true` means before-termination and `false` means after-termination. Unfortunately, this setting didn't affect the cleanup order upon donwstream cancellation and was always cleaning up the resource before canceling the upstream.

In 3.x, the cleanup order is now consistent when the sequence terminates or gets cancelled: `true` means before-termination or before canceling the upstream, `false` means after-termination or after canceling the upstream.

:information_source: **Further references:** Issue [#6347](https://github.com/ReactiveX/RxJava/pull/6347), PR [#6534](https://github.com/ReactiveX/RxJava/pull/6534)

# API changes

A major release allows cleaning up and improving the API surface by adding, changing or removing elements all across. With 3.x, there are several of such changes that require some explanations.

## Functional interfaces

RxJava 2.x introduced a custom set of functional interfaces in `io.reactivex.functions` so that the use of the library is possible with the same types on Java 6 and Java 8. A secondary reason for such custom types is that the standard Java 8 function types do not support throwing any checked exceptions, which in itself can result in some inconvenience when using RxJava operators.

Despite RxJava 3 being based on Java 8, the issues with the standard Java 8 functional interfaces persist, now with possible [desugaring](https://developer.android.com/studio/preview/features#j8-desugar) issues on Android and their inability to throw checked exceptions. Therefore, 3.x kept the custom interfaces, but the `@FunctionalInterface` annotation has been applied to them (which is safe/ignored on Android).

```java
@FunctionalInterface
interface Function<@NonNull T, @NonNull R> {
    R apply(T t) throws Throwable;
}
```

In addition, Java 8 allows declaring annotations on type argument and type argument use individually and thus all functional interfaces have received nullability annotations.

:information_source: **Further references:** PR [#6840](https://github.com/ReactiveX/RxJava/pull/6840), PR [#6791](https://github.com/ReactiveX/RxJava/pull/6791), PR [#6795](https://github.com/ReactiveX/RxJava/pull/6795)

### Wider throws

One small drawback with the custom `throws Exception` in the functional interfaces is that some 3rd party APIs may throw a checked exception that is not a descendant of `Exception`, or simply throw `Throwable`.

Therefore, with 3.x, the functional interfaces as well as other support interfaces have been widened and declared with `throws Throwable` in their signature.

This widening should be inconsequential for lambda-based or class-implementations provided to the RxJava methods:

```java
source.map(v -> {
    if (v == 0) {
        throw new Exception();
    }
    return v;
});

source.filter(new Predicate<Integer>() {
    @Override
    public boolean test() throws Exception {
        throw new IOException();
    }
});
```

I.e., there is no need to change `throws Exception` to `throws Throwable` just for the sake of it.

However, if one uses these functional interfaces outside:

```java
static void Integer callFunction(
        Function<Integer, Integer> function, Integer value) throws Exception {
    return function.apply(value);
}
```

the widening of `throws` will have to be propagated:

```java
static void Integer callFunction(
        Function<Integer, Integer> function, Integer value) throws Throwable {
    return function.apply(value);
}
```

:information_source: **Further references:** PR [#6511](https://github.com/ReactiveX/RxJava/pull/6511), PR [#6579](https://github.com/ReactiveX/RxJava/pull/6579)

## New Types

### Supplier

RxJava 2.x already supported the standard `java.util.concurrent.Callable` whose `call` method is declared with `throws Exception` by default. Unfortunately, when our custom functional interfaces were [widened to `throws Throwable`](#widen-throws), it was impossible to widen `Callable` because in Java, implementations can't widen the `throws` clause, only narrow or abandon it.

Therefore, 3.x introduces the `io.reactivex.rxjava3.functions.Supplier` interface that defines the widest `throws` possible:

```java
interface Supplier<@NonNull R> {
    R get() throws Throwable;
}
```

<a name="#supplier"><a href="#supplier">⚠️</a> **Note on running "Organize Imports" from the IDE**

Due to naming matches, IDE's tend to import `java.util.function.Supplier` instead of picking RxJava's `io.reactivex.rxjava3.functions.Supplier`. Also IDEs tend to give non-descriptive errors such as "Suppliercan't be converted to Supplier", omitting the fact about the package differences.

<a name="#supplier"><a href="#supplier">⚠️</a> **Signature change**

To comply with the support for wider throws functional interfaces, many operators used to take `java.util.concurrent.Callable` now take `io.reactivex.rxjava3.functions.Supplier` instead. If the operator was used with a lambda, only recompilation is needed:

```java
Flowable.defer(() -> Flowable.just(Math.random()));
```

However, if explicit implementation was used:

```java
Flowable.defer(new Callable<Double>() {
    @Override
    public Double call() throws Exception {
        return Math.random();
    }
});
```

the **interface type** (`Callable` -> `Supplier`) and the **method name** (`call` -> `get`) has to be adjusted:

```java
Flowable.defer(new Supplier<Double>() {
    @Override
    public Double get() throws Exception {
        return Math.random();
    }
});
```

See the [API signature changes](#api-signature-changes) section on which operators are affected.

:information_source: **Further references:** PR [#6511](https://github.com/ReactiveX/RxJava/pull/6511)

### Converters

In 2.x, the `to()` operator used the generic `Function` to allow assembly-time conversion of flows into arbitrary types. The drawback of this
approach was that each base reactive type had the same `Function` interface in their method signature, 
thus it was impossible to implement multiple converters for different reactive types within the same class. 
To work around this issue, the `as` operator and `XConverter` interfaces have been introduced
in 2.x, which interfaces are distinct and can be implemented on the same class. Changing the signature of `to` in 2.x was not possible due
to the pledged binary compatibility of the library.

From 3.x, the `as()` methods have been removed and the `to()` methods now each work with their respective `XConverter` interfaces (hosted in package `io.reactivex.rxjava3.core`):

- `Flowable.to(Function<Flowable<T>, R>)` -> `Flowable.to(FlowableConverter<T, R>)`
- `Observable.to(Function<Observable<T>, R>)` -> `Observable.to(ObservableConverter<T, R>)`
- `Maybe.to(Function<Flowable<T>, R>)` -> `Maybe.to(MaybeConverter<T, R>)`
- `Single.to(Function<Flowable<T>, R>)` -> `Maybe.to(SingleConverter<T, R>)`
- `Completable.to(Function<Completable, R>)` -> `Completable.to(CompletableConverter<R>)`
- `ParallelFlowable.to(Function<ParallelFlowable<T>, R)` -> `ParallelFlowable.to(ParallelFlowableConverter<T, R>)`

If one was using these methods with a lambda expression, only a recompilation is needed:

```java
// before
source.to(flowable -> flowable.blockingFirst());

// after
source.to(flowable -> flowable.blockingFirst());
```

If one was implementing a Function interface (typically anonymously), the interface type, type arguments and the `throws` clause have to be adjusted

```java
// before
source.to(new Function<Flowable<Integer>, Integer>() {
    @Override
    public Integer apply(Flowable<Integer> t) throws Exception {
        return t.blockingFirst();
    }
});

// after
source.to(new FlowableConverter<Integer, Integer>() {
    @Override
    public Integer apply(Flowable<Integer> t) {
        return t.blockingFirst();
    }
});
```

:information_source: **Further references:**  Issue [#5654](https://github.com/ReactiveX/RxJava/pull/5654), PR [#6514](https://github.com/ReactiveX/RxJava/pull/6514)

## Moved components

### Disposables

Moving to Java 8 and Android's [desugaring](https://developer.android.com/studio/preview/features#j8-desugar) tooling allows the use of static interface methods instead of separate factory classes. The support class `io.reactivex.disposables.Disposables` was a prime candidate for moving all of its methods into the `Disposable` interface itself (`io.reactivex.rxjava3.disposables.Disposable`).

Uses of the factory methods:

```java
Disposable d = Disposables.empty();
```

should now be turned into:

```java
Disposable d = Disposable.empty();
```

:information_source: **Further references:**  PR [#6781](https://github.com/ReactiveX/RxJava/pull/6781)

### DisposableContainer

Internally, RxJava 2.x uses an abstraction of a disposable container instead of using `CompositeDisposable` everywhere, allowing a more appropriate container type to be used. This is achieved via an internal `DisposableContainer` implemented by `CompositeDisposable` as well as other internal components. Unfortunately, since the public class referenced an internal interface, RxJava was causing warnings in OSGi environments.

In RxJava 3, the `DisposableContainer` is now part of the public API under `io.reactivex.rxjava3.disposables.DisposableContainer` and no longer causes OSGi issues.

:information_source: **Further references:**  Issue [#6742](https://github.com/ReactiveX/RxJava/issues/6742), PR [#6745](https://github.com/ReactiveX/RxJava/pull/6745)

## API promotions

The RxJava 2.2.x line has still a couple of [**experimental**](https://github.com/ReactiveX/RxJava#experimental) operators (but no [**beta**](https://github.com/ReactiveX/RxJava#beta)) operators, which have been promoted to standard with 3.x:

### Flowable promotions

- [`dematerialize(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#dematerialize-io.reactivex.rxjava3.functions.Function-)

### Observable promotions

- [`dematerialize(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#dematerialize-io.reactivex.rxjava3.functions.Function-)

### Maybe promotions

- [`doOnTerminate(Action)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#doOnTerminate-io.reactivex.rxjava3.functions.Action-)
- [`materialize()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#materialize--)

### Single promotions

- [`dematerialize(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#dematerialize-io.reactivex.rxjava3.functions.Function-)
- [`materialize()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#materialize--)

### Completable promotions

- [`delaySubscription(long, TimeUnit)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#delaySubscription-long-java.util.concurrent.TimeUnit-)
- [`delaySubscription(long, TimeUnit, Scheduler)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#delaySubscription-long-java.util.concurrent.TimeUnit-io.reactivex.rxjava3.core.Scheduler-)
- [`materialize()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#materialize--)

:information_source: **Further references:**  PR [#6537](https://github.com/ReactiveX/RxJava/pull/6537)

## API additions

RxJava 3 received a considerable amount of new operators and methods across its API surface. Brand new operators introduced are marked with ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) in their respective **Available in:** listings

### replay with eagerTruncate

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Completable`

A limitation with the bounded `replay` operator is that to allow continuous item delivery to slow consumers, a linked list of the cached items has to be maintained. By default, the head node of this list is moved forward when the boundary condition (size, time) mandates it. This setup avoids allocation in exchange for retaining one "invisible" item in the linked list. However, sometimes this retention is unwanted and the allocation overhead of a clean node is acceptable. In 2.x, the `ReplaySubject` and `ReplayProcessor` implementations already allowed for such behavior, but the instance `replay()` operators did not.

With 3.x, the `replay` operators (both connectable and multicasting variants) received overloads, defining an `eagerTruncate` option that performs this type of head node cleanup.

#### Flowable

- [`replay(int, boolean)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#replay-int-boolean-)
- [`replay(long, TimeUnit, Scheduler, boolean)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#replay-long-java.util.concurrent.TimeUnit-io.reactivex.rxjava3.core.Scheduler-boolean-)
- [`replay(int, long, TimeUnit, Scheduler, boolean)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#replay-int-long-java.util.concurrent.TimeUnit-io.reactivex.rxjava3.core.Scheduler-boolean-)
- [`replay(Function, int, boolean)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#replay-io.reactivex.rxjava3.functions.Function-int-boolean-)
- [`replay(Function, long, TimeUnit, Scheduler, boolean)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#replay-io.reactivex.rxjava3.functions.Function-long-java.util.concurrent.TimeUnit-io.reactivex.rxjava3.core.Scheduler-boolean-)
- [`replay(Function, int, long, TimeUnit, Scheduler, boolean)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#replay-io.reactivex.rxjava3.functions.Function-int-long-java.util.concurrent.TimeUnit-io.reactivex.rxjava3.core.Scheduler-boolean-)

#### Observable

- [`replay(int, boolean)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#replay-int-boolean-)
- [`replay(long, TimeUnit, Scheduler, boolean)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#replay-long-java.util.concurrent.TimeUnit-io.reactivex.rxjava3.core.Scheduler-boolean-)
- [`replay(int, long, TimeUnit, Scheduler, boolean)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#replay-int-long-java.util.concurrent.TimeUnit-io.reactivex.rxjava3.core.Scheduler-boolean-)
- [`replay(Function, int, boolean)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#replay-io.reactivex.rxjava3.functions.Function-int-boolean-)
- [`replay(Function, long, TimeUnit, Scheduler, boolean)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#replay-io.reactivex.rxjava3.functions.Function-long-java.util.concurrent.TimeUnit-io.reactivex.rxjava3.core.Scheduler-boolean-)
- [`replay(Function, int, long, TimeUnit, Scheduler, boolean)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#replay-io.reactivex.rxjava3.functions.Function-int-long-java.util.concurrent.TimeUnit-io.reactivex.rxjava3.core.Scheduler-boolean-)

:information_source: **Further references:**  Issue [#6475](https://github.com/ReactiveX/RxJava/issues/6475), PR [#6532](https://github.com/ReactiveX/RxJava/pull/6532)

### concatMap with Scheduler

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Completable`

A property of the `concatMap` operator is that the `mapper` function may be invoked either on the subscriber's thread or the currently completing inner source's thread. There is no good way to control this thread of invocation from the outside, therefore, new overloads have been added in 3.x with an additional `Scheduler` parameter:

#### Flowable

- [`concatMap(Function, int, Scheduler)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#concatMap-io.reactivex.rxjava3.functions.Function-int-io.reactivex.rxjava3.core.Scheduler-)
- [`concatMapDelayError(Function, int, boolean, Scheduler)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#concatMapDelayError-io.reactivex.rxjava3.functions.Function-boolean-int-io.reactivex.rxjava3.core.Scheduler-)

#### Observable

- [`concatMap(Function, int, Scheduler)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#concatMap-io.reactivex.rxjava3.functions.Function-int-io.reactivex.rxjava3.core.Scheduler-)
- [`concatMapDelayError(Function, int, boolean, Scheduler)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#concatMapDelayError-io.reactivex.rxjava3.functions.Function-boolean-int-io.reactivex.rxjava3.core.Scheduler-)

:information_source: **Further references:**  Issue [#6447](https://github.com/ReactiveX/RxJava/issues/6447), PR [#6538](https://github.com/ReactiveX/RxJava/pull/6538)

### Schedulers.from fair mode

By default, `Schedulers.from` executes work on the supplied `Executor` in an eager mode, running as many tasks as available. This can cause some unwanted lack of interleaving between these tasks and external tasks submitted to the same executor. To remedy the situation, a new mode and overload has been added so that the `Scheduler` returned by `Schedulers.from` runs tasks one by one, allowing other external tasks to be interleaved.

- [`Schedulers.from(Executor, boolean, boolean)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/schedulers/Schedulers.html#from-java.util.concurrent.Executor-boolean-boolean-)

:information_source: **Further references:**  Issue [#6696](https://github.com/ReactiveX/RxJava/issues/6447), Issue [#6697](https://github.com/ReactiveX/RxJava/issues/6697), PR [#6744](https://github.com/ReactiveX/RxJava/pull/6744)

### blockingForEach with buffer size

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Completable`

The underlying `blockingIterable` operator had already the option to specify the internal buffer size (and prefetch amounts), which is now exposed via new `blockingForEach` overloads

- [`Flowable.blockingForEach(Consumer, int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#blockingForEach-io.reactivex.rxjava3.functions.Consumer-int-)
- [`Observable.blockingForEach(Consumer, int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#blockingForEach-io.reactivex.rxjava3.functions.Consumer-int-)

:information_source: **Further references:**  Issue [#6784](https://github.com/ReactiveX/RxJava/issues/6784), PR [#6800](https://github.com/ReactiveX/RxJava/pull/6800)

### blockingSubscribe

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Completable`

For API consistency, the callback-based `blockingSubscribe` methods have been introduced to `Maybe`, `Single` and `Completable` respectively.

#### Maybe

- [`blockingSubscribe()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#blockingSubscribe--)
- [`blockingSubscribe(Consumer)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#blockingSubscribe-io.reactivex.rxjava3.functions.Consumer-)
- [`blockingSubscribe(Consumer, Consumer)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#blockingSubscribe-io.reactivex.rxjava3.functions.Consumer-io.reactivex.rxjava3.functions.Consumer-)
- [`blockingSubscribe(Consumer, Consumer, Action)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#blockingSubscribe-io.reactivex.rxjava3.functions.Consumer-io.reactivex.rxjava3.functions.Consumer-io.reactivex.rxjava3.functions.Action-)
- [`blockingSubscribe(MaybeObserver)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#blockingSubscribe-io.reactivex.rxjava3.core.MaybeObserver-)

#### Single

- [`blockingSubscribe()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#blockingSubscribe--)
- [`blockingSubscribe(Consumer)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#blockingSubscribe-io.reactivex.rxjava3.functions.Consumer-)
- [`blockingSubscribe(Consumer, Consumer)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#blockingSubscribe-io.reactivex.rxjava3.functions.Consumer-io.reactivex.rxjava3.functions.Consumer-)
- [`blockingSubscribe(SingleObserver)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#blockingSubscribe-io.reactivex.rxjava3.core.SingleObserver-)

#### Completable

- [`blockingSubscribe()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#blockingSubscribe--)
- [`blockingSubscribe(Action)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#blockingSubscribe-io.reactivex.rxjava3.functions.Action-)
- [`blockingSubscribe(Action, Consumer)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#blockingSubscribe-io.reactivex.rxjava3.functions.Action-io.reactivex.rxjava3.functions.Consumer-)
- [`blockingSubscribe(CompletableObserver)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#blockingSubscribe-io.reactivex.rxjava3.core.CompletableObserver-)

:information_source: **Further references:**  Issue [#6852](https://github.com/ReactiveX/RxJava/issues/6852), PR [#6862](https://github.com/ReactiveX/RxJava/pull/6862)

### Maybe.delay with delayError

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Completable`

The option, available in every other reactive type, to delay the errors optionally as well was missing from `Maybe`.

- [`delay(long, TimeUnit, boolean)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#delay-long-java.util.concurrent.TimeUnit-boolean-)
- [`delay(long, TimeUnit, Scheduler, boolean)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#delay-long-java.util.concurrent.TimeUnit-io.reactivex.rxjava3.core.Scheduler-boolean-)

:information_source: **Further references:**  Issue [#6863](https://github.com/ReactiveX/RxJava/issues/6863), PR [#6864](https://github.com/ReactiveX/RxJava/pull/6864)

### onErrorComplete

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Completable`

Upon an error, the sequence is completed (conditionally) instead of signaling the error.

#### Flowable

- [`onErrorComplete()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#onErrorComplete--)
- [`onErrorComplete()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#onErrorComplete-io.reactivex.rxjava3.functions.Predicate-)

#### Observable

- [`onErrorComplete()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#onErrorComplete--)
- [`onErrorComplete()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#onErrorComplete-io.reactivex.rxjava3.functions.Predicate-)


#### Single

- [`onErrorComplete()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#onErrorComplete--)
- [`onErrorComplete()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#onErrorComplete-io.reactivex.rxjava3.functions.Predicate-)


:information_source: **Further references:**  Issue [#6852](https://github.com/ReactiveX/RxJava/issues/6852), PR [#6867](https://github.com/ReactiveX/RxJava/pull/6867)

### Completable.onErrorResumeWith

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Completable`

This operator (under the name `onErrorResumeNext` now renamed) was already available everywhere else and was accidentally left out of `Completable`.

- [`onErrorResumeWith(Completable)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#onErrorResumeWith-io.reactivex.rxjava3.core.CompletableSource-)

:information_source: **Further references:**  Issue [#6852](https://github.com/ReactiveX/RxJava/issues/6852), PR [#6868](https://github.com/ReactiveX/RxJava/pull/6868)

### retryUntil

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Completable`

The operator was missing from `Single` and `Completable`.

- [`Single.retryUntil(BooleanSupplier)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#retryUntil-io.reactivex.rxjava3.functions.BooleanSupplier-)
- [`Completable.retryUntil(BooleanSupplier)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#retryUntil-io.reactivex.rxjava3.functions.BooleanSupplier-)

:information_source: **Further references:**  Issue [#6852](https://github.com/ReactiveX/RxJava/issues/6852), PR [#6869](https://github.com/ReactiveX/RxJava/pull/6869)

### switchOnNext

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Completable`

Added the static version of the `switchMap` operator, `switchOnNext` and `switchOnNextDelayError`, to `Maybe`, `Single` and `Completable`.

- [`Maybe.switchOnNext(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#switchOnNext-org.reactivestreams.Publisher-)
- [`Single.switchOnNext(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#switchOnNext-org.reactivestreams.Publisher-)
- [`Completable.switchOnNext(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#switchOnNext-org.reactivestreams.Publisher-)
- [`Maybe.switchOnNextDelayError(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#switchOnNextDelayError-org.reactivestreams.Publisher-)
- [`Single.switchOnNextDelayError(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#switchOnNextDelayError-org.reactivestreams.Publisher-)
- [`Completable.switchOnNextDelayError(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#switchOnNextDelayError-org.reactivestreams.Publisher-)

:information_source: **Further references:**  Issue [#6852](https://github.com/ReactiveX/RxJava/issues/6852), PR [#6870](https://github.com/ReactiveX/RxJava/pull/6870)

### Maybe.dematerialize

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Completable`

The operator was already added to the other reactive types before.

- [`dematerialize(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#dematerialize-io.reactivex.rxjava3.functions.Function-)

:information_source: **Further references:**  Issue [#6852](https://github.com/ReactiveX/RxJava/issues/6852), PR [#6871](https://github.com/ReactiveX/RxJava/pull/6871)

### from conversions

Several operators have been added across:

Operator | F | O | M | S | C |
-|-|-|-|-|-|
<a name='fromAction'></a>`fromAction`|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png)|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png)|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png)|![absent](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) <sup title='Never empty.'>([23](https://github.com/ReactiveX/RxJava/wiki/Operator-Matrix#notes-23))</sup>|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png)|
<a name='fromCompletable'></a>`fromCompletable`|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png)|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png)|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png)|![absent](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) <sup title='Always error.'>([72](https://github.com/ReactiveX/RxJava/wiki/Operator-Matrix#notes-72))</sup>|![absent](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) <sup title='Use wrap().'>([73](#notes-73))</sup>|
<a name='fromMaybe'></a>`fromMaybe`|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png)|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png)|![absent](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) <sup title='Use wrap().'>([73](https://github.com/ReactiveX/RxJava/wiki/Operator-Matrix#notes-73))</sup>|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png)|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png)|
<a name='fromObservable'></a>`fromObservable`|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png)|![absent](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) <sup title='Use wrap().'>([73](https://github.com/ReactiveX/RxJava/wiki/Operator-Matrix#notes-73))</sup>|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png)|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png)|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png)|
<a name='fromPublisher'></a>`fromPublisher`|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png)|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png)|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png)|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png)|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png)|
<a name='fromRunnable'></a>`fromRunnable`|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png)|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png)|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png)|![absent](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) <sup title='Never empty.'>([23](https://github.com/ReactiveX/RxJava/wiki/Operator-Matrix#notes-23))</sup>|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png)|
<a name='fromSingle'></a>`fromSingle`|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png)|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png)|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png)|![absent](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) <sup title='Use wrap().'>([73](https://github.com/ReactiveX/RxJava/wiki/Operator-Matrix#notes-73))</sup>|![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png)|

#### Flowable

- [`fromAction(Action)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#fromAction-io.reactivex.rxjava3.functions.Action-)
- [`fromCompletable(CompletableSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#fromCompletable-io.reactivex.rxjava3.core.CompletableSource-)
- [`fromMaybe(MaybeSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#fromMaybe-io.reactivex.rxjava3.core.MaybeSource-)
- [`fromObservable(ObservableSource, BackpressureStrategy)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#fromObservable-io.reactivex.rxjava3.core.ObservableSource-io.reactivex.rxjava3.core.BackpressureStrategy-)
- [`fromRunnable(Runnable)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#fromRunnable-java.lang.Runnable-)
- [`fromSingle(Runnable)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#fromSingle-io.reactivex.rxjava3.core.SingleSource-)

#### Observable

- [`fromAction(Action)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#fromAction-io.reactivex.rxjava3.functions.Action-)
- [`fromCompletable(CompletableSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#fromCompletable-io.reactivex.rxjava3.core.CompletableSource-)
- [`fromMaybe(MaybeSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#fromMaybe-io.reactivex.rxjava3.core.MaybeSource-)
- [`fromRunnable(Runnable)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#fromRunnable-java.lang.Runnable-)
- [`fromSingle(Runnable)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#fromSingle-io.reactivex.rxjava3.core.SingleSource-)

#### Maybe

- [`fromObservable(ObservableSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#fromObservable-io.reactivex.rxjava3.core.ObservableSource-)
- [`fromPublisher(Publisher)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#fromPublisher-org.reactivestreams.Publisher-)

#### Single

- [`fromMaybe(ObservableSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#fromMaybe-io.reactivex.rxjava3.core.MaybeSource-)

:information_source: **Further references:**  Issue [#6852](https://github.com/ReactiveX/RxJava/issues/6852), PR [#6873](https://github.com/ReactiveX/RxJava/pull/6873)

### timestamp and timeInterval

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Completable`

These operators were already available for `Flowable` and `Observable`, now added to `Single` and `Maybe`.

#### Maybe

- [`timeInterval()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#timeInterval--)
- [`timeInterval(TimeUnit)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#timeInterval-java.util.concurrent.TimeUnit-)
- [`timeInterval(Scheduler)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#timeInterval-io.reactivex.rxjava3.core.Scheduler-)
- [`timeInterval(TimeUnit, Scheduler)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#timeInterval-java.util.concurrent.TimeUnit-io.reactivex.rxjava3.core.Scheduler-)
- [`timestamp()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#timestamp--)
- [`timestamp(TimeUnit)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#timestamp-java.util.concurrent.TimeUnit-)
- [`timestamp(Scheduler)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#timestamp-io.reactivex.rxjava3.core.Scheduler-)
- [`timestamp(TimeUnit, Scheduler)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#timestamp-java.util.concurrent.TimeUnit-io.reactivex.rxjava3.core.Scheduler-)

#### Single

- [`timeInterval()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#timeInterval--)
- [`timeInterval(TimeUnit)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#timeInterval-java.util.concurrent.TimeUnit-)
- [`timeInterval(Scheduler)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#timeInterval-io.reactivex.rxjava3.core.Scheduler-)
- [`timeInterval(TimeUnit, Scheduler)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#timeInterval-java.util.concurrent.TimeUnit-io.reactivex.rxjava3.core.Scheduler-)
- [`timestamp()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#timestamp--)
- [`timestamp(TimeUnit)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#timestamp-java.util.concurrent.TimeUnit-)
- [`timestamp(Scheduler)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#timestamp-io.reactivex.rxjava3.core.Scheduler-)
- [`timestamp(TimeUnit, Scheduler)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#timestamp-java.util.concurrent.TimeUnit-io.reactivex.rxjava3.core.Scheduler-)

:information_source: **Further references:**  Issue [#6852](https://github.com/ReactiveX/RxJava/issues/6852), PR [#6874](https://github.com/ReactiveX/RxJava/pull/6874)

### toFuture

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Completable`

This operator was already available elsewhere, now added to `Maybe` and `Completable`.

- [`Maybe.toFuture()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#toFuture--)
- [`Completable.toFuture()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#toFuture--)

:information_source: **Further references:**  Issue [#6852](https://github.com/ReactiveX/RxJava/issues/6852), PR [#6875](https://github.com/ReactiveX/RxJava/pull/6875)

### ofType

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Completable`

This operator was already available in `Flowable` and `Observable`, now added to `Maybe` and `Single`.

- [`Maybe.ofType(Class)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#ofType-java.lang.Class-)
- [`Single.ofType(Class)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#ofType-java.lang.Class-)

:information_source: **Further references:**  Issue [#6852](https://github.com/ReactiveX/RxJava/issues/6852), PR [#6876](https://github.com/ReactiveX/RxJava/pull/6876)

### doOnLifecycle

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Completable`

This operator was already available in `Flowable` and `Observable`, now added to `Maybe`, `Single` and `Completable`.

- [`Maybe.doOnLifecycle()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#doOnLifecycle-io.reactivex.rxjava3.functions.Consumer-io.reactivex.rxjava3.functions.Action-)
- [`Single.doOnLifecycle()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#doOnLifecycle-io.reactivex.rxjava3.functions.Consumer-io.reactivex.rxjava3.functions.Action-)
- [`Completable.doOnLifecycle()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#doOnLifecycle-io.reactivex.rxjava3.functions.Consumer-io.reactivex.rxjava3.functions.Action-)

:information_source: **Further references:**  Issue [#6852](https://github.com/ReactiveX/RxJava/issues/6852), PR [#6877](https://github.com/ReactiveX/RxJava/pull/6877)

### concatMap to another type

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Completable`

Added varios concatMap-based transformations between `Maybe`, `Single` and `Completable` for `Maybe` and `Single`. These are essentially aliases to the respective `flatMap` operators for better discoverability.

- [`Maybe.concatMapCompletable(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#concatMapCompletable-io.reactivex.rxjava3.functions.Function-)
- [`Maybe.concatMapSingle(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#concatMapSingle-io.reactivex.rxjava3.functions.Function-)
- [`Single.concatMapCompletable(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#concatMapCompletable-io.reactivex.rxjava3.functions.Function-)
- [`Single.concatMapMaybe(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#concatMapMaybe-io.reactivex.rxjava3.functions.Function-)
- [`Single.concatMap(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#concatMap-io.reactivex.rxjava3.functions.Function-)

:information_source: **Further references:**  Issue [#6852](https://github.com/ReactiveX/RxJava/issues/6852), PR [#6879](https://github.com/ReactiveX/RxJava/pull/6879)

### concat with delayError

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Completable`

The delayError variants of the `concat` operator were missing across.

#### Maybe

- [`Maybe.concatArrayEagerDelayError(Maybe...)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#concatArrayEagerDelayError-io.reactivex.rxjava3.core.MaybeSource...-)
- [`Maybe.concatDelayError(Publisher, int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#concatDelayError-org.reactivestreams.Publisher-int-)

#### Single

- [`Single.concatArrayDelayError(Single...)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#concatArrayDelayError-io.reactivex.rxjava3.core.SingleSource...-)
- [`Single.concatArrayEagerDelayError`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#concatArrayEagerDelayError-io.reactivex.rxjava3.core.SingleSource...-)
- [`Single.concatDelayError(Iterable)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#concatDelayError-java.lang.Iterable-)
- [`Single.concatDelayError(Publisher)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#concatDelayError-org.reactivestreams.Publisher-)
- [`Single.concatDelayError(Publisher, int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#concatDelayError-org.reactivestreams.Publisher-int-)

#### Completable

- [`Completable.concatArrayDelayError(Completable...)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#concatArrayDelayError-io.reactivex.rxjava3.core.CompletableSource...-)
- [`Completable.concatDelayError(Iterable)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#concatDelayError-java.lang.Iterable-)
- [`Completable.concatDelayError(Publisher)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#concatDelayError-org.reactivestreams.Publisher-)
- [`Completable.concatDelayError(Publisher, int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#concatDelayError-org.reactivestreams.Publisher-int-)

:information_source: **Further references:**  Issue [#6852](https://github.com/ReactiveX/RxJava/issues/6852), PR [#6881](https://github.com/ReactiveX/RxJava/pull/6881)

### Single.mergeArray

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Completable`

The operator was already available elsewhere, now added to `Single`.

- [`mergeArray(SingleSource...)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#mergeArray-io.reactivex.rxjava3.core.SingleSource...-)
- [`mergeArrayDelayError(SingleSource...)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#mergeArrayDelayError-io.reactivex.rxjava3.core.SingleSource...-)

:information_source: **Further references:**  Issue [#6852](https://github.com/ReactiveX/RxJava/issues/6852), PR [#6882](https://github.com/ReactiveX/RxJava/pull/6882)

### Completable.sequenceEqual

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Completable`

The operator was already available elsewhere, now added to `Completable`.

- [`sequenceEqual`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#sequenceEqual-io.reactivex.rxjava3.core.CompletableSource-io.reactivex.rxjava3.core.CompletableSource-)

:information_source: **Further references:**  Issue [#6852](https://github.com/ReactiveX/RxJava/issues/6852), PR [#6884](https://github.com/ReactiveX/RxJava/pull/6884)

### startWith

**Available in:**

source \ other | F | O | M | S | C |
--|--|--|--|--|--|
Flowable | ![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) | ![absent](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) | ![add](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) | ![add](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) | ![add](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png)
Observable | ![absent](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) | ![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png)| ![add](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) | ![add](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) | ![add](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png)
Maybe | ![add](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) | ![add](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) | ![add](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) | ![add](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) | ![add](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png)
Single | ![add](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) | ![add](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) | ![add](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) | ![add](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) | ![add](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png)
Completable | ![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) | ![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) | ![add](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) | ![add](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) | ![present](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png)

Added overloads for better continuation support between the reactive types.

### Flowable

- [`startWith(MaybeSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#startWith-io.reactivex.rxjava3.core.CompletableSource-)
- [`startWith(SingleSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#startWith-io.reactivex.rxjava3.core.SingleSource-)
- [`startWith(CompletableSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#startWith-io.reactivex.rxjava3.core.CompletableSource-)

### Observable

- [`startWith(MaybeSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#startWith-io.reactivex.rxjava3.core.MaybeSource-)
- [`startWith(SingleSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#startWith-io.reactivex.rxjava3.core.SingleSource-)
- [`startWith(CompletableSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#startWith-io.reactivex.rxjava3.core.CompletableSource-)

### Maybe

- [`startWith(Publisher)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#startWith-org.reactivestreams.Publisher-)
- [`startWith(ObservableSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#startWith-io.reactivex.rxjava3.core.ObservableSource-)
- [`startWith(MaybeSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#startWith-io.reactivex.rxjava3.core.MaybeSource-)
- [`startWith(SingleSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#startWith-io.reactivex.rxjava3.core.SingleSource-)
- [`startWith(CompletableSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#startWith-io.reactivex.rxjava3.core.CompletableSource-)

### Single

- [`startWith(Publisher)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#startWith-org.reactivestreams.Publisher-)
- [`startWith(ObservableSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#startWith-io.reactivex.rxjava3.core.ObservableSource-)
- [`startWith(MaybeSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#startWith-io.reactivex.rxjava3.core.MaybeSource-)
- [`startWith(SingleSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#startWith-io.reactivex.rxjava3.core.SingleSource-)
- [`startWith(CompletableSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#startWith-io.reactivex.rxjava3.core.CompletableSource-)

### Completable

- [`startWith(MaybeSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#startWith-io.reactivex.rxjava3.core.MaybeSource-)
- [`startWith(SingleSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#startWith-io.reactivex.rxjava3.core.SingleSource-)

:information_source: **Further references:**  Issue [#6852](https://github.com/ReactiveX/RxJava/issues/6852), PR [#6885](https://github.com/ReactiveX/RxJava/pull/6885)

### Completable.onErrorReturn

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Completable`

The operators `onErrorReturn` and `onErrorReturnItem` weres available everywhere else and are now added to `Completable`.

- [`onErrorReturn`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#onErrorReturn-io.reactivex.rxjava3.functions.Function-)
- [`onErrorReturnItem`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#onErrorReturnItem-T-)

:information_source: **Further references:**  Issue [#6852](https://github.com/ReactiveX/RxJava/issues/6852), PR [#6886](https://github.com/ReactiveX/RxJava/pull/6886)

### safeSubscribe

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Completable`

The method was already available in `Flowable` and `Observable`, now added to `Maybe`, `Single` and `Completable` for API consistency.

- [`Maybe.safeSubscribe(MaybeObserver)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#safeSubscribe-io.reactivex.rxjava3.core.MaybeObserver-)
- [`Single.safeSubscribe(SingleObserver)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#safeSubscribe-io.reactivex.rxjava3.core.SingleObserver-)
- [`Completable.safeSubscribe(CompletableObserver)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#safeSubscribe-io.reactivex.rxjava3.core.CompletableObserver-)

:information_source: **Further references:**  Issue [#6852](https://github.com/ReactiveX/RxJava/issues/6852), PR [#6887](https://github.com/ReactiveX/RxJava/pull/6887)

### Single.flatMap 

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Completable`

Add two overloads of `flatMap` to `Single`: one to transform the success or error signals into a new `SingleSource`, one to combine the original success value with the success value of the inner sources:

- [`flatMap(Function, Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#flatMap-io.reactivex.rxjava3.functions.Function-io.reactivex.rxjava3.functions.Function-)
- [`flatMap(Function, BiFunction)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#flatMap-io.reactivex.rxjava3.functions.Function-io.reactivex.rxjava3.functions.BiFunction-)

:information_source: **Further references:**  Issue [#6852](https://github.com/ReactiveX/RxJava/issues/6852), PR [#6893](https://github.com/ReactiveX/RxJava/pull/6893)

### concatEager and concatEagerDelayError

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Completable`

Add various `concatEager` and `concatEagerDelayError` overloads across the reactive types.

#### Flowable

- [`concatEagerDelayError(Iterable)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#concatEagerDelayError-java.lang.Iterable-)
- [`concatEagerDelayError(Iterable, int, int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#concatEagerDelayError-java.lang.Iterable-int-int-)
- [`concatEagerDelayError(Publisher)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#concatEagerDelayError-org.reactivestreams.Publisher-)
- [`concatEagerDelayError(Publisher, int, int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#concatEagerDelayError-org.reactivestreams.Publisher-int-int-)

### Observable

- [`concatEagerDelayError(Iterable)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#concatEagerDelayError-java.lang.Iterable-)
- [`concatEagerDelayError(Iterable, int, int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#concatEagerDelayError-java.lang.Iterable-int-int-)
- [`concatEagerDelayError(Publisher)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#concatEagerDelayError-org.reactivestreams.Publisher-)
- [`concatEagerDelayError(Publisher, int, int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#concatEagerDelayError-org.reactivestreams.Publisher-int-int-)

### Maybe

- [`concatEager(Iterable, int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#concatEager-java.lang.Iterable-int-)
- [`concatEager(Publisher, int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#concatEager-org.reactivestreams.Publisher-int-)
- [`concatEagerDelayError(Iterable)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#concatEagerDelayError-java.lang.Iterable-)
- [`concatEagerDelayError(Iterable, int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#concatEagerDelayError-java.lang.Iterable-int-)
- [`concatEagerDelayError(Publisher)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#concatEagerDelayError-org.reactivestreams.Publisher-)
- [`concatEagerDelayError(Publisher, int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#concatEagerDelayError-org.reactivestreams.Publisher-int-)

### Single

- [`concatEager(Iterable, int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#concatEager-java.lang.Iterable-int-)
- [`concatEager(Publisher, int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#concatEager-org.reactivestreams.Publisher-int-)
- [`concatEagerDelayError(Iterable)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#concatEagerDelayError-java.lang.Iterable-)
- [`concatEagerDelayError(Iterable, int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#concatEagerDelayError-java.lang.Iterable-int-)
- [`concatEagerDelayError(Publisher)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#concatEagerDelayError-org.reactivestreams.Publisher-)
- [`concatEagerDelayError(Publisher, int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#concatEagerDelayError-org.reactivestreams.Publisher-int-)

:information_source: **Further references:**  Issue [#6880](https://github.com/ReactiveX/RxJava/issues/6880), PR [#6899](https://github.com/ReactiveX/RxJava/pull/6899)

### fromSupplier

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Completable`

With the new type [`io.reactivex.rxjava3.functions.Supplier`](#supplier) comes a new wrapper operator `fromSupplier` to complement `fromCallable` in all the reactive types.

- [`Flowable.fromSupplier`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#fromSupplier-io.reactivex.rxjava3.functions.Supplier-)
- [`Observable.fromSupplier`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#fromSupplier-io.reactivex.rxjava3.functions.Supplier-)
- [`Maybe.fromSupplier`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#fromSupplier-io.reactivex.rxjava3.functions.Supplier-)
- [`Single.fromSupplier`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#fromSupplier-io.reactivex.rxjava3.functions.Supplier-)
- [`Completable.fromSupplier`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#fromSupplier-io.reactivex.rxjava3.functions.Supplier-)

:information_source: **Further references:** PR [#6529](https://github.com/ReactiveX/RxJava/pull/6529)

### ParallelFlowable.flatMapIterable

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_on.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Completable`<br>![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `ParallelFlowable`

The operator was already available in `Flowable` and `Observable`, now added to `ParallelFlowable`.

- [`flatMapIterable(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/parallel/ParallelFlowable.html#flatMapIterable-io.reactivex.rxjava3.functions.Function-)
- [`flatMapIterable(Function, int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/parallel/ParallelFlowable.html#flatMapIterable-io.reactivex.rxjava3.functions.Function-int-)

### flatMapIterable example

```java
Flowable.range(1, 10)
.parallel()
.runOn(Schedulers.computation())
.flatMapIterable(v -> Arrays.asList(v, v + 1));
```

:information_source: **Further references:**  PR [#6798](https://github.com/ReactiveX/RxJava/pull/6798)

## Java 8 additions

Now that the API baseline is set to Java 8, RxJava can now support the new types of Java 8 directly, without the need of an external library (such as the [RxJavaJdk8Interop](https://github.com/akarnokd/RxJavaJdk8Interop#rxjavajdk8interop) library, now discontinued).

:warning: Note that the Android [desugar](https://developer.android.com/studio/preview/features#j8-desugar) may not support all Java 8 APIs for all target possible Android API levels, however, their mere existence in the RxJava class files should not cause any trouble.

### Java 8 functional interfaces

:warning: RxJava 3 doesn't support working with Java 8 functional interfaces directly because it prefers its own custom set of functional interfaces with a wider range of platform support and exception handling.

However, Java 8 has language support for a relatively convenient way to convert a Java 8 functional interface to its RxJava 3 equivalent via method handles:

```java
java.util.function.Function<Integer, Integer> f = a -> a + 1;

Flowable.range(1, 10)
.map(f::apply)
;

// or
io.reactivex.rxjava3.functions.Function<Integer, Integer> f2 = f::apply;
```

Unfortunately, the reverse direction is not possible because Java 8's functional interfaces do not allow throwing a checked exception.

In general, the distinction between the two sets of interfaces shouldn't be a practical problem because unlike Java 8's `java.util.Collectors`, there is no repository of pre-made functional interface implementations out there that would require more direct support from RxJava. 

### fromOptional

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Completable`

Given an existing, constant reference of a `java.util.Optional`, turn it into a `Flowable`, `Observable` or `Maybe` source, emitting its value immediately or completing immediately.

:bulb: There is no `Single` variant because it *has to be non-empty*. No `Completable` either because *it is always empty*.

- [`Flowable.fromOptional`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#fromOptional-java.util.Optional-)
- [`Observable.fromOptional`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#fromOptional-java.util.Optional-)
- [`Maybe.fromOptional`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#fromOptional-java.util.Optional-)

#### fromOptional example

```java
Flowable<Integer> zero = Flowable.fromOptional(Optional.empty());

Observable<Integer> one = Flowable.fromOptional(Optional.of(1));

Maybe<Integer> maybe = Flowable.fromOptional(Optional.ofNullable(valueMaybeNull));
```

:information_source: **Further references:**  Issue [#6776](https://github.com/ReactiveX/RxJava/issues/6776), PR [#6765](https://github.com/ReactiveX/RxJava/pull/6765), PR [#6783](https://github.com/ReactiveX/RxJava/pull/6783), PR [#6797](https://github.com/ReactiveX/RxJava/pull/6797)

### fromStream

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Completable`

Turns a `java.util.stream.Stream` into a `Flowable` or `Observable` and emits its items to consumers.

:bulb: Because `Stream` is assumed to be having zero to N items (possibly infinite), there is no good way to expose it as `Maybe`, `Single` or `Completable`.

:warning: RxJava 3 doesn't accept the primitive `Stream` types (such as `IntStream` and `DoubleStream`). These streams have to be converted into their boxed variants via their `boxed()` method. Since RxJava uses reference types, there is no way to optimize the interoperation with the primitive streams.

- [`Flowable.fromStream`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#fromStream-java.util.stream.Stream-)
- [`Observable.fromStream`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#fromStream-java.util.stream.Stream-)

#### fromStream example

```java
Flowable<Integer> stream = Flowable.fromStream(IntStream.range(1, 10).boxed());

Observable<Integer> stream2 = Observable.fromStream(list.stream());
```

:information_source: **Further references:**  Issue [#6776](https://github.com/ReactiveX/RxJava/issues/6776), PR [#6765](https://github.com/ReactiveX/RxJava/pull/6765), PR [#6797](https://github.com/ReactiveX/RxJava/pull/6797)

### fromCompletionStage

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Completable`

Wrap a `java.util.concurrent.CompletionStage` instance (such as `CompletableFuture`) into a reactive type and expose its single value or failure as the appropriate reactive signal.

:bulb: A `CompletionStage` is like a hot source that is already executing or has already terminated, thus the wrapper is only there to observe the outcome, not to initiate the computation the stage represents.

:warning: Note that the standard Java 8 `CompletionStage` interface doesn't support cancellation, thus canceling the reactive flow will not stop the given `CompletionStage`.

- [`Flowable.fromCompletionStage`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#fromCompletionStage-java.util.concurrent.CompletionStage-)
- [`Observable.fromCompletionStage`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#fromCompletionStage-java.util.concurrent.CompletionStage-)
- [`Maybe.fromCompletionStage`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#fromCompletionStage-java.util.concurrent.CompletionStage-)
- [`Single.fromCompletionStage`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#fromCompletionStage-java.util.concurrent.CompletionStage-)
- [`Completable.fromCompletionStage`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#fromCompletionStage-java.util.concurrent.CompletionStage-)

#### fromCompletionStage example

```java
Flowable<Integer> someAsync = Flowable.fromCompletionStage(
    operation.getAsync()
);

Obervable<Integer> otherAsync = Observable.fromCompletionStage(
    CompletableFuture.completedFuture(1)
);

Maybe<Object> failed = Maybe.fromCompletionStage(
    CompletableFurure.completedFuture(0)
    .thenAccept(v -> { throw new RuntimeException(); })
```

:information_source: **Further references:**  Issue [#6776](https://github.com/ReactiveX/RxJava/issues/6776), PR [#6765](https://github.com/ReactiveX/RxJava/pull/6765), PR [#6783](https://github.com/ReactiveX/RxJava/pull/6783), PR [#6797](https://github.com/ReactiveX/RxJava/pull/6797)

### mapOptional

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Completable`<br>
![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `ParallelFlowable`

Transform the upstream item(s) into `java.util.Optional` instances, then emit the non-empty value, or if the `Optional` is empty, skip to the next upstream value.

:bulb: `Completable` has no items to map.

- [`Flowable.mapOptional`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#mapOptional-io.reactivex.rxjava3.functions.Function-)
- [`Observable.mapOptional`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#mapOptional-io.reactivex.rxjava3.functions.Function-)
- [`Maybe.mapOptional`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#mapOptional-io.reactivex.rxjava3.functions.Function-)
- [`Single.mapOptional`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#mapOptional-io.reactivex.rxjava3.functions.Function-)
- [`ParallelFlowable.mapOptional(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/parallel/ParallelFlowable.html#mapOptional-io.reactivex.rxjava3.functions.Function-)
- [`ParallelFlowable.mapOptional(Function, BiFunction)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/parallel/ParallelFlowable.html#mapOptional-io.reactivex.rxjava3.functions.Function-io.reactivex.rxjava3.functions.BiFunction-)
- [`ParallelFlowable.mapOptional(Function, ParallelFailureHandling)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/parallel/ParallelFlowable.html#mapOptional-io.reactivex.rxjava3.functions.Function-io.reactivex.rxjava3.parallel.ParallelFailureHandling-)

#### mapOptional example

```java
Flowable.range(1, 10)
.mapOptional(v -> v % 2 == 0 ? Optional.of(v) : Optional.empty());

Flowable.range(1, 10)
.parallel()
.runOn(Schedulers.computation())
.mapOptional(v -> v % 2 == 0 ? Optional.of(v) : Optional.empty());
.sequential();
```

:information_source: **Further references:**  Issue [#6776](https://github.com/ReactiveX/RxJava/issues/6776), PR [#6775](https://github.com/ReactiveX/RxJava/pull/6775), PR [#6783](https://github.com/ReactiveX/RxJava/pull/6783), PR [#6797](https://github.com/ReactiveX/RxJava/pull/6797), PR [#6798](https://github.com/ReactiveX/RxJava/pull/6798)

### collect with Collector

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Completable`<br>
![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `ParallelFlowable`

Provides the ability to aggregate items of a `Flowable` or `Observable` with the help of Java 8's rich set of `Collector` implementations. See [`Collectors`](https://docs.oracle.com/javase/8/docs/api/java/util/stream/Collectors.html) for its capabilities.

:bulb: Because a sequence is assumed to be having zero to N items (possibly infinite), there is no good reason to collect a `Maybe`, `Single` or `Completable`.

- [`Flowable.collect(Collector)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#collect-java.util.stream.Collector-)
- [`Observable.collect(Collector)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#collect-java.util.stream.Collector-)
- [`ParallelFlowable.collect(Collector)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/parallel/ParallelFlowable.html#collect-java.util.stream.Collector-)

#### collect example

```java
Single<List<Integer>> list = Flowable.range(1, 10)
.collect(Collectors.toList());

Flowable<List<Integr>> list2 = Flowable.range(1, 10)
.parallel()
.runOn(Schedulers.computation())
.collect(Collectors.toList());
```

:information_source: **Further references:**  Issue [#6776](https://github.com/ReactiveX/RxJava/issues/6776), PR [#6775](https://github.com/ReactiveX/RxJava/pull/6775), PR [#6797](https://github.com/ReactiveX/RxJava/pull/6797), PR [#6798](https://github.com/ReactiveX/RxJava/pull/6798)

### firstStage, singleStage, lastStage

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Completable`

Expose the first, only or very last item of a `Flowable` or `Observable` as a `java.util.concurrent.CompletionStage`.

:bulb: For `Maybe`, `Single` and `Completable`, the equivalent operator is called [`toCompletionStage`](#tocompletionstage).

:bulb: Since a sequence can be empty, there are two variants to these methods: one that takes a default value for such an empty source and one that signals a `NoSuchElementException` via the returned `CompletionStage`. These latter methods have the [OrError](#firstorerrorstage-singleorerrorstage-lastorerrorstage) in their method name.

- [`Flowable.firstStage(T)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#firstStage-T-)
- [`Flowable.singleStage(T)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#singleStage-T-)
- [`Flowable.lastStage(T)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#lastStage-T-)
- [`Observable.firstStage(T)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#firstStage-T-)
- [`Observable.singleStage(T)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#singleStage-T-)
- [`Observable.lastStage(T)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#lastStage-T-)

#### stage examples

```java
// Signals 1
CompletionStage<Integer> cs = Flowable.range(1, 10)
    .firstStage(11);

// Signals IndexOutOfBoundsException as the source has too many items
CompletionStage<Integer> cs1 = Flowable.just(1, 2)
    .singleStage(11);

// Signals 11
CompletionStage<Integer> cs2 = Observable.<Integer>empty()
    .lastStage(11);
```

:information_source: **Further references:**  Issue [#6776](https://github.com/ReactiveX/RxJava/issues/6776), PR [#6775](https://github.com/ReactiveX/RxJava/pull/6775), PR [#6797](https://github.com/ReactiveX/RxJava/pull/6797)

### firstOrErrorStage, singleOrErrorStage, lastOrErrorStage

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Completable`

Expose the first, only or very last item of a `Flowable` or `Observable` as a `java.util.concurrent.CompletionStage`, or
signal `NoSuchElementException` of the source sequence is empty..

:bulb: For `Maybe`, `Single` and `Completable`, the equivalent operator is called [`toCompletionStage`](#tocompletionstage).

:bulb: Since a sequence can be empty, there are two variants to these methods: one that takes a default value for such an empty source and one that signals a `NoSuchElementException` via the returned `CompletionStage`. The [former](#firststage-singlestage-laststage) do not have the `OrError` in their method name.

- [`Flowable.firstStage()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#firstOrErrorStage--)
- [`Flowable.singleStage()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#singleOrErrorStage--)
- [`Flowable.lastStage()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#lastOrErrorStage--)
- [`Observable.firstStage()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#firstOrErrorStage--)
- [`Observable.singleStage()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#singleOrErrorStage--)
- [`Observable.lastStage()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#lastOrErrorStage--)

#### stage examples

```java
// Signals 1
CompletionStage<Integer> cs = Flowable.range(1, 10)
    .firstOrErrorStage();

// Signals IndexOutOfBoundsException as the source has too many items
CompletionStage<Integer> cs1 = Flowable.just(1, 2)
    .singleOrErrorStage();

// Signals NoSuchElementException
CompletionStage<Integer> cs2 = Observable.<Integer>empty()
    .lastOrErrorStage();
```

:information_source: **Further references:**  Issue [#6776](https://github.com/ReactiveX/RxJava/issues/6776), PR [#6775](https://github.com/ReactiveX/RxJava/pull/6775), PR [#6797](https://github.com/ReactiveX/RxJava/pull/6797)

### toCompletionStage

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Completable`

Expose the sigle value or termination of a `Maybe`, `Single` or `Completable` as a `java.util.concurrent.CompletionStage`.

:bulb: The equivalent operators in `Flowable` and `Observable` are called [`firstStage`, `singleStage`, `lastStage`](#firststage-singlestage-laststage), [`firstOrErrorStage`, `singleOrErrorStage` and `lastOrErrorStage`](#firstorerrorstage-singleorerrorstage-lastorerrorstage).

:bulb: The `Maybe` and `Completable` operators allow defining a default completion value in case the source turns out to be empty.

- [`Maybe.toCompletionStage()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#toCompletionStage--)
- [`Maybe.toCompletionStage()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#toCompletionStage-T-)
- [`Single.toCompletionStage()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#toCompletionStage--)
- [`Completable.toCompletionStage()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#toCompletionStage-T-)

#### toCompletionStage example

```java
// Signals 1
CompletionStage<Integer> cs = Maybe.just(1).toCompletionStage();

// Signals NoSuchElementException
CompletionStage<Integer> cs = Maybe.empty().toCompletionStage();

// Signals 10
CompletionStage<Integer> cs = Maybe.empty().toCompletionStage(10);

// Signals 10
CompletionStage<String> cs2 = Completable.empty().toCompletionStage(10);
```

:information_source: **Further references:**  Issue [#6776](https://github.com/ReactiveX/RxJava/issues/6776), PR [#6783](https://github.com/ReactiveX/RxJava/pull/6783)

### blockingStream

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Completable`

Exposes a `Flowable` or an `Observable` as a blocking `java.util.stream.Stream`.

:bulb: Streams are expected to have zero to N (possibly infinite) elements and thus there is no good reason to stream
a `Maybe`, `Single` or `Completable`. Use the appropriate `blockingGet` and `blockingAwait` methods instead.

:warning: Abandoning a `Stream` may cause leaks or computations running indefinitely. It is recommended one closes the `Stream` manually or via the **try-with-resources** construct of Java 7+.

- [`Flowable.blockingStream()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#blockingStream--)
- [`Flowable.blockingStream(int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#blockingStream-int-)
- [`Observable.blockingStream()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#blockingStream--)
- [`Observable.blockingStream(int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#blockingStream-int-)

### blockingStream example

```java
try (Stream stream = Flowable.range(1, 10)
    .subscribeOn(Schedulers.computation())
    .blockingStream()) {

   stream.limit(5)
   .forEach(System.out::println);
}
```

:information_source: **Further references:**  Issue [#6776](https://github.com/ReactiveX/RxJava/issues/6776), PR [#6779](https://github.com/ReactiveX/RxJava/pull/6779), PR [#6797](https://github.com/ReactiveX/RxJava/pull/6797)

### flatMapStream, concatMapStream

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Completable`<br>
![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `ParallelFlowable`

Maps each upstream item to a `java.util.stream.Stream` and emits those inner items, in sequence, non-overlappingly to the downstream.

:bulb: `flatMapStream` and `concatMapStream` are essentially the same operators because consuming a `Stream` is a sequential (and perhaps blocking) operation, thus there is no way two or more distinct `Stream`s could get interleaved.

:bulb: Since a `Stream` can be exposed as both backpressure-supporting `Flowable` or a backpressure-unsupporting `Observable`, the equivalent operators for `Maybe` and `Single` are called [`flattenStreamAsFlowable` and `flattenStreamAsObservable`](#flattenstreamasflowable-flattenstreamasobservable).

:warning: RxJava 3 doesn't accept the primitive `Stream` types (such as `IntStream` and `DoubleStream`). These streams have to be converted into their boxed variants via their `boxed()` method. Since RxJava uses reference types, there is no way to optimize the interoperation with the primitive streams.

- [`Flowable.concatMapStream(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#concatMapStream-io.reactivex.rxjava3.functions.Function-)
- [`Flowable.concatMapStream(Function, int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#concatMapStream-io.reactivex.rxjava3.functions.Function-int-)
- [`Flowable.flatMapStream(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#flatMapStream-io.reactivex.rxjava3.functions.Function-)
- [`Flowable.flatMapStream(Function, int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#flatMapStream-io.reactivex.rxjava3.functions.Function-int-)
- [`Observable.concatMapStream(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#concatMapStream-io.reactivex.rxjava3.functions.Function-)
- [`Observable.flatMapStream(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#flatMapStream-io.reactivex.rxjava3.functions.Function-)
- [`ParallelFlowable.flatMapStream(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/parallel/ParallelFlowable.html#flatMapStream-io.reactivex.rxjava3.functions.Function-)
- [`ParallelFlowable.flatMapStream(Function, int)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/parallel/ParallelFlowable.html#flatMapStream-io.reactivex.rxjava3.functions.Function-int-)

#### flatMapStream example

```java
Flowable.range(1, 10)
   .flatMapStream(v -> Arrays.asList(v, v + 1).stream());

Observable.range(1, 10)
   .concatMapStream(v -> Arrays.asList(v, v + 1).stream());

Flowable.range(1, 10)
    .parallel()
    .runOn(Schedulers.computation())
    .flatMapStream(v -> Arrays.asList(v, v + 1).stream());
```

:information_source: **Further references:**  Issue [#6776](https://github.com/ReactiveX/RxJava/issues/6776), PR [#6779](https://github.com/ReactiveX/RxJava/pull/6779), PR [#6797](https://github.com/ReactiveX/RxJava/pull/6797), PR [#6798](https://github.com/ReactiveX/RxJava/pull/6798)

### flattenStreamAsFlowable, flattenStreamAsObservable

**Available in:** ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Flowable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Observable`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Maybe`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_half.png) `Single`, ![image](https://raw.github.com/wiki/ReactiveX/RxJava/images/checkmark_off.png) `Completable`

Maps success item into a `java.util.stream.Stream` and emits those inner items.

:bulb: The equivalent operator is called [`flatMapStream`](#flatmapstream-concatmapstream) in `Flowable`, `Observable` and `ParallelFlowable`.

:bulb: There are no `flattenStreamAs` methods in `Completable` because it is always empty and has no item to map.

:warning: RxJava 3 doesn't accept the primitive `Stream` types (such as `IntStream` and `DoubleStream`). These streams have to be converted into their boxed variants via their `boxed()` method. Since RxJava uses reference types, there is no way to optimize the interoperation with the primitive streams.

- [`Maybe.flattenStreamAsFlowable`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#flattenStreamAsFlowable-io.reactivex.rxjava3.functions.Function-)
- [`Maybe.flattenStreamAsObservable`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#flattenStreamAsObservable-io.reactivex.rxjava3.functions.Function-)
- [`Single.flattenStreamAsFlowable`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#flattenStreamAsFlowable-io.reactivex.rxjava3.functions.Function-)
- [`Single.flattenStreamAsObservable`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#flattenStreamAsObservable-io.reactivex.rxjava3.functions.Function-)

#### flattenStreamAs example

```java
Flowable<Integer> f = Maybe.just(1)
.flattenStreamAsFlowable(v -> Arrays.asList(v, v + 1).stream());

Observable<Integer> o = Single.just(2)
.flattenStreamAsObservable(v -> IntStream.range(v, v + 10).boxed());
```

:information_source: **Further references:**  Issue [#6776](https://github.com/ReactiveX/RxJava/issues/6776), PR [#6805](https://github.com/ReactiveX/RxJava/pull/6805)

## API renames

### startWith

The method was ambiguous and/or inviting wrong usage in other languages. They have now been renamed to `startWithArray`, `startWithIterable` and `startWithItem`:

#### Flowable

- [`startWithArray`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#startWithArray-T...-)
- [`startWithItem`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#startWithItem-T-)
- [`startWithIterable`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#startWithIterable-java.lang.Iterable-)

#### Observable

- [`startWithArray`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#startWithArray-T...-)
- [`startWithItem`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#startWithItem-T-)
- [`startWithIterable`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#startWithIterable-java.lang.Iterable-)

:information_source: **Further references:**  Issue [#6122](https://github.com/ReactiveX/RxJava/issues/6122), PR [#6530](https://github.com/ReactiveX/RxJava/pull/6530)

### onErrorResumeNext with source

The method was ambiguous and/or inviting wrong usage in other languages. They have now been renamed to `onErrorResumeWith` across all types.

- [`Flowable.onErrorResumeWith()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#onErrorResumeWith-org.reactivestreams.Publisher-)
- [`Observable.onErrorResumeWith()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#onErrorResumeWith-io.reactivex.rxjava3.core.ObservableSource-)
- [`Maybe.onErrorResumeWith()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#onErrorResumeWith-io.reactivex.rxjava3.core.MaybeSource-)
- [`Single.onErrorResumeWith()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#onErrorResumeWith-io.reactivex.rxjava3.core.SingleSource-)
- [`Completable.onErrorResumeWith()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Completable.html#onErrorResumeWith-io.reactivex.rxjava3.core.CompletableSource-)

:information_source: **Further references:**  Issue [#6551](https://github.com/ReactiveX/RxJava/issues/6551), PR [#6556](https://github.com/ReactiveX/RxJava/pull/6556)

### zipIterable

Renamed to be plain `zip` to match the naming convention with other operators (i.e., Iterable/Source versions are named plainly, array-versions receive an `Array` postfix).

- [Flowable.zip()](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#zip-java.lang.Iterable-io.reactivex.rxjava3.functions.Function-)
- [Observable.zip()](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#zip-java.lang.Iterable-io.reactivex.rxjava3.functions.Function-)

:information_source: **Further references:** Issue [#6610](https://github.com/ReactiveX/RxJava/issues/6610), PR [#6638](https://github.com/ReactiveX/RxJava/pull/6638)

### combineLatest with array argument

Renamed to be plain `combineLatestArray` and `combineLatestArrayDelayError` to match the naming convention with other operators (i.e., Iterable/Source versions are named plainly, array-versions receive an `Array` postfix).

- [`Flowable.combineLatestArray()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#combineLatestArray-org.reactivestreams.Publisher:A-io.reactivex.rxjava3.functions.Function-)
- [`Flowable.combineLatestArrayDelayError()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#combineLatestArrayDelayError-org.reactivestreams.Publisher:A-io.reactivex.rxjava3.functions.Function-)
- [`Observable.combineLatestArray()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#combineLatestArray-org.reactivestreams.Publisher:A-io.reactivex.rxjava3.functions.Function-)
- [`Observable.combineLatestArrayDelayError()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#combineLatestArrayDelayError-io.reactivex.rxjava3.core.ObservableSource:A-io.reactivex.rxjava3.functions.Function-)

:information_source: **Further references:** Issue [#6820](https://github.com/ReactiveX/RxJava/issues/6820), PR [#6640](https://github.com/ReactiveX/RxJava/pull/6640), PR [#6838](https://github.com/ReactiveX/RxJava/pull/6838)

### Single.equals

Renamed to `sequenceEqual` to match the naming in the other reactive classes.

- [`sequenceEqual(SingleSource, SingleSource)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#sequenceEqual-io.reactivex.rxjava3.core.SingleSource-io.reactivex.rxjava3.core.SingleSource-)

:information_source: **Further references:** Issue [#6854](https://github.com/ReactiveX/RxJava/issues/6854), PR [#6856](https://github.com/ReactiveX/RxJava/pull/6856)

### Maybe.flatMapSingleElement

The operator was confusing and has been renamed to `flatMapSingle`, replacing the original `Maybe.flatMapSingle`. The original behavior (i.e., signaling `NoSuchElementException` if the `Maybe` is empty) can be emulated via `toSingle()`.

```java
source.flatMapSingle(item -> singleSource).toSingle()
```

:information_source: **Further references:** Issue [#6878](https://github.com/ReactiveX/RxJava/issues/6878), PR [#6891](https://github.com/ReactiveX/RxJava/pull/6891)

## API signature changes

### Callable to Supplier

Operators accepting a `java.util.concurrent.Callable` have been changed to accept `io.reactivex.rxjava3.functions.Supplier` instead to enable the callbacks to [throw any](#wider-throws) kind of exceptions.

If the operator was used with a lambda, only a recompilation is needed:

```java
Flowable.defer(() -> Flowable.just(Math.random()));
```

However, if explicit implementation was used:

```java
Flowable.defer(new Callable<Double>() {
    @Override
    public Double call() throws Exception {
        return Math.random();
    }
});
```

the **interface type** (`Callable` -> `Supplier`) and the **method name** (`call` -> `get`) has to be adjusted:

```java
Flowable.defer(new Supplier<Double>() {
    @Override
    public Double get() throws Exception {
        return Math.random();
    }
});
```

#### Affected operators

(Across all reactive types, multiple overloads.)

| | | |
|--|--|--|
defer | error | using
generate | buffer | collect
distinct | reduceWith | scanWith
toMap | toMultimap |

:information_source: **Further references:**  PR [#6511](https://github.com/ReactiveX/RxJava/pull/6511)

### Maybe.defaultIfEmpty

Corrected the return type to `Single` as now it is guaranteed to have a success item or an error.

- [`defaultIfEmpty(T)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#defaultIfEmpty-T-)

:information_source: **Further references:**  PR [#6511](https://github.com/ReactiveX/RxJava/pull/6517)

### concatMapDelayError parameter order

Change the order of the `tillTheEnd` argument in `concatMapDelayError` and `concatMapEagerDelayError` to be consistent with other operators taking a boolean parameter before `prefetch`/`maxConcurrency`.

- [`Flowable.concatMapDelayError()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#concatMapDelayError-io.reactivex.rxjava3.functions.Function-boolean-int-)
- [`Flowable.concatMapEagerDelayError()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#concatMapEagerDelayError-io.reactivex.rxjava3.functions.Function-boolean-int-int-)
- [`Observable.concatMapDelayError()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#concatMapDelayError-io.reactivex.rxjava3.functions.Function-boolean-int-)
- [`Observable.concatMapEagerDelayError()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Observable.html#concatMapEagerDelayError-io.reactivex.rxjava3.functions.Function-boolean-int-int-)

:information_source: **Further references:** Issue [#6610](https://github.com/ReactiveX/RxJava/pull/6610), PR [#6638](https://github.com/ReactiveX/RxJava/pull/6638)

### Flowable.buffer with boundary source

The signature was wrongly declared with a `Flowable` instead of a more general `Publisher`.

- [`buffer(Publisher, Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#buffer-org.reactivestreams.Publisher-io.reactivex.rxjava3.functions.Function-)
- [`buffer(Publisher, Function, Supplier)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Flowable.html#buffer-org.reactivestreams.Publisher-io.reactivex.rxjava3.functions.Function-io.reactivex.rxjava3.functions.Supplier-)

:information_source: **Further references:** PR [#6858](https://github.com/ReactiveX/RxJava/pull/6858)

### Maybe.flatMapSingle

The operator was not in line with how `flatMap`s are expected to operate (i.e., it signaled `NoSuchElementException`
if the `Maybe` was empty). The `flatMapSingleElement` operator has been renamed to be the `flatMapSingle` operator. 

- [`flatMapSingle(Function)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#flatMapSingle-io.reactivex.rxjava3.functions.Function-)

The original error behavior can be emulated via `toSingle()`:

```java
source.flatMapSingle(item -> singleSource).toSingle()
```

:information_source: **Further references:** Issue [#6878](https://github.com/ReactiveX/RxJava/issues/6878), PR [#6891](https://github.com/ReactiveX/RxJava/pull/6891)

## API removals

### getValues (hot sources)

The `getValue()` and `getValues(T[])` methods were a remnant from a time where `Subject` and `FlowableProcessor` was unifying all state peeking methods for every kind of subject/processor. These have been marked as `@Deprecated` in 2.x and are now removed from 3.x. They can be trivially replaced with `getValue()` if necessary, for example:

```java
Object value = subject.getValue();
if (value == null) {
   return new Object[1];
}
return new Object[] { value };
```

:information_source: **Further references:**  Issue [#5622](https://github.com/ReactiveX/RxJava/issues/5622), PR [#6516](https://github.com/ReactiveX/RxJava/pull/6516)

### Maybe.toSingle(T)

Use [`Maybe.defaultIfEmpty(T)`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Maybe.html#defaultIfEmpty-T-) instead.

:information_source: **Further references:**  PR [#6517](https://github.com/ReactiveX/RxJava/pull/6517)

### subscribe(4 arguments)

Removed from `Flowable` and `Observable`. The 4th argument, the `Subscription`/`Disposable` callback, was more or less useless. Use `Flowable.doOnSubscribe()` and `Observable.doOnSubscribe()` instead. instead.

:information_source: **Further references:**  PR [#6517](https://github.com/ReactiveX/RxJava/pull/6517)

### Single.toCompletable()

Using a better terminology instead: [`ignoreElement()`](http://reactivex.io/RxJava/3.x/javadoc/io/reactivex/rxjava3/core/Single.html#ignoreElement--).

:information_source: **Further references:**  PR [#6517](https://github.com/ReactiveX/RxJava/pull/6517)

### Completable.blockingGet()

The behavior and signature were confusing (i.e., returning `null` or a `Throwable`). Use `blockingAwait()` instead.

:information_source: **Further references:**  PR [#6517](https://github.com/ReactiveX/RxJava/pull/6517)

### test support methods

Based on user feedback, the following methods have been removed from `TestSubscriber` and `TestObserver` respectively due to being less useful outside testing RxJava itself:

| | | |
|--|--|--|
assertErrorMessage | assertFailure(Predicate, T...) | assertFailureAndMessage
assertNever(Predicate) | assertNever(T) | assertNoTimeout
assertNotSubscribed | assertNotTerminated | assertSubscribed
assertTerminated | assertTimeout | assertValueSequenceOnly
assertValueSet | assertValueSetOnly | awaitCount(int, Runnable)
awaitCount(int, Runnable, long) | awaitTerminalEvent | awaitTerminalEvent(long TimeUnit)
clearTimeout | completions | errorCount
errors | getEvents | isTerminated
isTimeout | lastThread | valueCount
assertOf

:information_source: **Further references:**  Issue [#6153](https://github.com/ReactiveX/RxJava/issues/6153), PR [#6526](https://github.com/ReactiveX/RxJava/pull/6526)

### replay with Scheduler

The`replay(Scheduler)` and other overloads were carried over from the original Rx.NET API set but appears to be unused. Most use cases capture the connectable anyway so there is no much benefit from inlining an `observeOn` into a connectable:

```java
ConnectableFlowable<Integer> connectable = source.replay();

Flowable<Integr> flowable = connectable.observeOn(Schedulers.io());

// hand flowable to consumers
flowable.subscribe();

connectable.connect();
```

:information_source: **Further references:** PR [#6539](https://github.com/ReactiveX/RxJava/pull/6539)

### dematerialize()

The `Flowable.dematerialize()` and `Observable.dematerialize()` were inherently type-unsafe and have been removed. In Rx.NET, the extension methods allowed `dematerialize()` to be applied to `Observable<Notification<T>>` only, but there is no way for doing it in Java as it has no extension methods and one can't restrict a method to appear only with a certain type argument scheme.

Use `deserialize(Function)` instead.

```java
Observable<Notification<Integer>> source = ...

Observable<Integer> result = source.dematerialize(v -> v);
```

:information_source: **Further references:** PR [#6539](https://github.com/ReactiveX/RxJava/pull/6539)

### onExceptionResumeNext

The operator was apparently not used anywhere and has been removed from all types. It's function can be emulated via `onErrorResumeNext`: 

```java
source.onErrorResumeNext(
    error -> error instanceof Exception 
        ? fallback : Obserable.error(error))
```

:information_source: **Further references:** Issue [#6554](https://github.com/ReactiveX/RxJava/issues/6554), PR [#6564](https://github.com/ReactiveX/RxJava/pull/6564), PR [#6844](https://github.com/ReactiveX/RxJava/pull/6844)

### buffer with boundary supplier

This operator did not see much use and have been removed from `Flowable` and `Observable`. It can be emulated with the plain [sourced version](http://reactivex.io/RxJava/2.x/javadoc/io/reactivex/Flowable.html#buffer-org.reactivestreams.Publisher-):

```java
source.buffer(Observable.defer(supplier).take(1).repeat())
```

:information_source: **Further references:** Issue [#6555](https://github.com/ReactiveX/RxJava/issues/6555), PR [#6564](https://github.com/ReactiveX/RxJava/pull/6564)

### combineLatest with varags

Both the vararg overloaded versions of `combineLatest` and `combineLatestDelayError` were awkward to use from other JVM languages and have been removed. Use `combineLatestArray` and `combineLatestArrayDelayError` instead.

:information_source: **Further references:** Issue [#6634](https://github.com/ReactiveX/RxJava/issues/6634), PR [#6635](https://github.com/ReactiveX/RxJava/pull/6635)

### zip with nested source

Zip requires a known number of sources to work with. These overloads were just collecting up the inner sources for another overload. Removed from both `Flowable` and `Observable`. They can be emulated via composition:

```java
Observable<Observable<Integer>> sources = ...

sources.toList().flatMapObservable(list -> Observable.zip(list, zipper));
```

:information_source: **Further references:** PR [#6638](https://github.com/ReactiveX/RxJava/pull/6638)

### fromFuture with scheduler

These were just convenience overloads for `fromFuture().subscribeOn()` all across. Apply `subscribeOn` explicitly from now on.

```java
Flowable.fromFuture(future).subscribeOn(Schedulers.io());

Flowable.fromFuture(future, 5, TimeUnit.SECONDS)
    .subscribeOn(Schedulers.io());
```

:information_source: **Further references:** Issue [#6811](https://github.com/ReactiveX/RxJava/issues/6811), PR [#6814](https://github.com/ReactiveX/RxJava/pull/6814)

### Observable.concatMapIterable with buffer parameter

This overload had no effect because there is no buffering happening inside the operator (unlike in the `Flowable` variant). Use the `Observable.concatMapIterable(Function)` overload instead.

:information_source: **Further references:** Issue [#6828](https://github.com/ReactiveX/RxJava/issues/6828), PR [#6837](https://github.com/ReactiveX/RxJava/pull/6837)

# Interoperation

## Reactive Streams

RxJava 3 still follows the Reactive Streams specification and as such, the `io.reactivex.rxjava3.core.Flowable` is a compatible source for any 3rd party solution accepting an `org.reactivestreams.Publisher` as input.

`Flowable` can also wrap any such `org.reactivestreams.Publisher` in return.

:information_source: Note that it is possible to interface RxJava's 2.x `Flowable` and 3.x `Flowable` this way, however, due to the specification requirements, this involves extra overhead. Instead, one should use a [dedicated interoperation library](#rxjava-2x).

## RxJava 1.x

RxJava is more than 7 years old at this moment and many users are still stuck with 3rd party tools or libraries only supporting the RxJava 1 line.

To help with the situation, and also help with a gradual migration from 1.x to 3.x, an external interop library is provided:

https://github.com/akarnokd/RxJavaInterop#rxjavainterop

## RxJava 2.x

Migration from 2.x to 3.x could also be cumbersome as well as difficult because the 2.x line also amassed an ecosystem of tools and libraries of its own, which may take time to provide a native 3.x versions.

RxJava 3.x was structured, both in code and in Maven coordinates, to allow the existence of both 2.x and 3.x code side by side (or even have all 3 major versions at once).

There is limited interoperation between the `Flowable`s through the Reactive Streams `Publisher` interface (although not recommended due to extra overheads), however, there is no direct way for a 2.x `Observable` to talk to a 3.x `Observable` as they are completely separate types.

To help with the situation, and also help with a gradual migration from 2.x to 3.x, an external interop library is provided:

https://github.com/akarnokd/RxJavaBridge#rxjavabridge

## Java 9

The move to a Java 8 baseline was enabled by Android's improved (and upcoming) [desugaring](https://developer.android.com/studio/preview/features#j8-desugar) toolset.

Unfortunately, there was no indication if and when this tooling would support Java 9, more specifically, the `java.util.concurrent.Flow` interfaces imported and standardized from the 3rd party Reactive Streams specification.

There is a semi-hidden `org.reactivestreams.FlowAdapter` class in the Reactive Streams library that could be used for conversion in-between, but yet again, it adds some extra overhead.

Therefore, an external, native interoperation library is provided to convert between `java.util.concurrent.Flow.Publisher` and `io.reactivex.rxjava3.core.Flowable` as well as `java.util.concurrent.Flow.Processor` and `io.reactivex.rxjava3.processors.FlowableProcessor`.

https://github.com/akarnokd/RxJavaJdk9Interop#rxjavajdk9interop

:bulb: Conversion to other RxJava 3 reactive types are not supported and the user is expected to apply the appropriate RxJava 3 [conversion method](https://github.com/ReactiveX/RxJava#converting-to-the-desired-type).

## Swing

Since the Graphical User Interface library [Swing](https://docs.oracle.com/javase/8/docs/api/javax/swing/package-summary.html) is not part of the Android platform, the desktop users of the JDK have to resort to an external library to work with GUI components and their event sources:

https://github.com/akarnokd/RxJavaSwing#rxjavaswing

## Project Loom

There is a project in the works at Oracle trying to solve the asynchronous programming problems in a different way than RxJava and **reactive programming** has been doing it for  more than a decade.

[The idea](https://wiki.openjdk.java.net/display/loom/Main) is to have the user code appear to be imperative and blocking, but the JVM will make it so that actual, and resource-limited, native OS threads don't get blocked.

:warning: Note that *Project Loom* is currently incomplete and keeps changing its surface API from preview to preview. Every new preview version may require rework in the respective user and interop implementations again and again.

It could be years till the design and implementation of *Project Loom* becomes mainstream in the JDK, and perhaps even more time until Android picks it up. Therefore, to allow early experimentation, an external library is provided to allow working with generators written in an imperative and (virtually) blocking fashion:

https://github.com/akarnokd/RxJavaFiberInterop#rxjavafiberinterop

:bulb: Since Project Loom offers a transparent way of turning blocking operations (such as `CountDownLatch.await()`) into economic virtual thread suspensions, there is no need to provide any specific conversion method from RxJava 3 to *Project Loom*; executing any of the standard RxJava `blockingXXX` method in a virtual thread automatically benefits from this transparent suspension.

# Miscellaneous

## Changelog of the individual release candidates

- [3.0.0-RC0](https://github.com/ReactiveX/RxJava/releases/tag/v3.0.0-RC0)
- [3.0.0-RC1](https://github.com/ReactiveX/RxJava/releases/tag/v3.0.0-RC1)
- [3.0.0-RC2](https://github.com/ReactiveX/RxJava/releases/tag/v3.0.0-RC2)
- [3.0.0-RC3](https://github.com/ReactiveX/RxJava/releases/tag/v3.0.0-RC3)
- [3.0.0-RC4](https://github.com/ReactiveX/RxJava/releases/tag/v3.0.0-RC4)
- [3.0.0-RC5](https://github.com/ReactiveX/RxJava/releases/tag/v3.0.0-RC5)
- [3.0.0-RC6](https://github.com/ReactiveX/RxJava/releases/tag/v3.0.0-RC6)
- [3.0.0-RC7](https://github.com/ReactiveX/RxJava/releases/tag/v3.0.0-RC7)
- [3.0.0-RC8](https://github.com/ReactiveX/RxJava/releases/tag/v3.0.0-RC8)
- [3.0.0-RC9](https://github.com/ReactiveX/RxJava/releases/tag/v3.0.0-RC9)
