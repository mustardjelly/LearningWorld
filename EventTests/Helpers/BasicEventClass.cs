using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static UnitTestProject1.TextFromatter.TextFormatter;

namespace UnitTestProject1.EventTests.Helpers
{
    /// <summary>
    /// Contains skeletal code for event testing.
    /// </summary>
    public class BasicEventClass
    {
        internal int BasicEventsCounter = 0;
        /// <summary>
        /// Default Constructor.
        /// </summary>
        /// <remarks>
        /// Subscribes a 
        /// </remarks>
        public BasicEventClass()
        {
            Print($"Subscribed {nameof(DisplayBasicEventCounter)} to {nameof(BasicEvent)}", printKind: TextFromatter.PrintKind.Section);
            BasicEvent += DisplayBasicEventCounter;
        }

        public event EventHandler BasicEvent;


        public void RaiseBasicEventWithNoArgs()
        {
            var handler = BasicEvent;
            handler?.Invoke(this, new EventArgs());
        }

        /// <summary>
        /// Displays the number of times the event has been invoked.
        /// </summary>
        /// <param name="sender">Does nothing with this.</param>
        /// <param name="eventArgs">Does nothing with this.</param>
        private void DisplayBasicEventCounter(object sender, EventArgs eventArgs)
        {
            string eventString = $"{nameof(BasicEvent)}: {++BasicEventsCounter}";
            Print(eventString);
        }
    }
}
