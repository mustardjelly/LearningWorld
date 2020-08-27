using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace UnitTestProject1.TextFromatter
{
    internal static class TextFormatter
    {
        internal static void Print(string message, PrintType printType = PrintType.Console, PrintKind printKind = PrintKind.Emphasis)
        {
            string stringToPrint = string.Empty;
            switch (printKind)
            {
                case PrintKind.Emphasis:
                    stringToPrint = Emphasis(message);
                    break;
                case PrintKind.Section:
                    stringToPrint = Section(message);
                    break;
            }

            switch (printType)
            {
                case PrintType.Console:
                    Console.WriteLine(stringToPrint);
                    break;
                default:
                    throw new NotImplementedException();
            }
        }

        internal static string Emphasis(string formatString)
        {
            var stringToFormat = new StringBuilder(3);

            CreateTextBuffer(in stringToFormat, formatString);
            stringToFormat.AppendLine();
            stringToFormat.AppendLine(formatString);
            CreateTextBuffer(in stringToFormat, formatString);

            return stringToFormat.ToString();
        }

        internal static string Section(string formatString)
        {
            var stringToFormat = new StringBuilder(2);
            stringToFormat.AppendLine(formatString);

            return stringToFormat.ToString();
        }

        private static void CreateTextBuffer(in StringBuilder stringToPrint, string formatString)
        {
            for (int i = 0; i < formatString.Length; i++)
            {
                stringToPrint.Append("=");
            }
        }
    }

    internal enum PrintType
    {
        Console
    }

    internal enum PrintKind
    {
        Emphasis,
        Section
    }
}
