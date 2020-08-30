using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace UnitTestProject1.EventTests.Helpers
{
    internal static class BasicEventClassExtension
    {

        private static int basicEventSubscribeCount = 0;
        internal static void SafeSubscribe(this BasicEventClass eventClass, EventHandler InvokableMethod)
        {
            if (basicEventSubscribeCount > 0)
            {
                Console.WriteLine($"Could not subscribe. Event subscription count: {basicEventSubscribeCount}");
                return;
            }

            Console.WriteLine($"Subscribed {nameof(InvokableMethod)} to {nameof(eventClass.BasicEvent)}.");
            basicEventSubscribeCount++;
            eventClass.BasicEvent += InvokableMethod;
        }

        internal static void SafeUnsubscribe(this BasicEventClass eventClass, EventHandler InvokableMethod)
        {
            if (basicEventSubscribeCount == 0)
            {
                Console.WriteLine($"Not subscribed!");
                return;
            }

            basicEventSubscribeCount = 0;
            eventClass.BasicEvent -= InvokableMethod;
        }
    }
}
