﻿using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using UnitTestProject1.EventTests.Helpers;

namespace UnitTestProject1.EventTests
{
    [TestClass]
    public class BasicEventClassTests
    {
        private BasicEventClass eventClass;
        private int counter = 0;

        void InvokableMethod(object sender, EventArgs eventArgs)
        {
            Console.WriteLine($"{counter++}: Invokable method invoked!");
        }

        [TestMethod]
        public void SubscribeAndInvoke()
        {
            eventClass = new BasicEventClass();
            eventClass.BasicEvent += InvokableMethod;
            eventClass.RaiseBasicEventWithNoArgs();
        }

        [TestMethod]
        public void SubscribeMultipleTimesAndInvoke()
        {
            int times = 10;

            eventClass = new BasicEventClass();
            for (int i = 0; i < times; i++)
            {
                eventClass.BasicEvent += InvokableMethod;
            }

            eventClass.RaiseBasicEventWithNoArgs();
        }

        [TestMethod]
        public void SubscribeAndInvokeMultipleTimes()
        {
            int times = 10;

            eventClass = new BasicEventClass();
            eventClass.BasicEvent += InvokableMethod;

            for (int i = 0; i < times; i++)
            {
                eventClass.RaiseBasicEventWithNoArgs();
            }
        }

        void InvokableMethod2(object sender, EventArgs eventArgs)
        {
            Console.WriteLine("Invokable method 2 invoked!");
        }

        [TestMethod]
        public void SubscribeOrderingAndInvoke()
        {
            eventClass = new BasicEventClass();
            eventClass.BasicEvent += InvokableMethod;
            eventClass.BasicEvent += InvokableMethod2;

            eventClass.RaiseBasicEventWithNoArgs();
            eventClass.RaiseBasicEventWithNoArgs();
        }

        [TestMethod]
        public void SubscribeUnsubscribeAndInvoke()
        {
            eventClass = new BasicEventClass();
            eventClass.BasicEvent += InvokableMethod;
            eventClass.BasicEvent -= InvokableMethod;

            eventClass.RaiseBasicEventWithNoArgs();
        }

        [TestMethod]
        public void SubscribeUnsubscribeAndInvoke2()
        {
            int subscribeCount = 10;
            int unsubscribeCount = 5;

            eventClass = new BasicEventClass();

            var subscribe = new Action(() => eventClass.BasicEvent += InvokableMethod);
            ActionExecutor(subscribe, subscribeCount);
            var unsubscribe = new Action(() => eventClass.BasicEvent -= InvokableMethod);
            ActionExecutor(unsubscribe, unsubscribeCount);

            eventClass.RaiseBasicEventWithNoArgs();
        }

        private void ActionExecutor(Action action, int times)
        {
            for (int i = 0; i < times; i++)
            {
                action.Invoke();
            }
        }
    }
}
