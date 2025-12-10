// C# version
using System;
using System.Collections.Generic;

class Loops {
    static void Main() {
        List<string> fruits = new List<string> { "apple", "banana", "pear" };
        foreach (string fruit in fruits) {
            Console.WriteLine("I like " + fruit);
        }
    }
}
