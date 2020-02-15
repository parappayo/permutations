using System;
using System.Collections;
using System.Collections.Generic;

namespace BushidoBurrito.Permutations
{
    class Permutations : IEnumerable<string>
    {
        private readonly string _input;

        public Permutations(string input)
        {
            _input = input;
        }

        public IEnumerator<string> GetEnumerator()
        {
            if (_input.Length < 2)
            {
                yield return _input;
                yield break;
            }

            var first = _input[0];
            var rest = _input.Substring(1);

            foreach (var subPerm in new Permutations(rest))
            {
                for (int i = 0; i <= subPerm.Length; i++)
                {
                    yield return $"{subPerm.Substring(0, i)}{first}{subPerm.Substring(i)}";
                }
            }
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            foreach (var p in new Permutations(args[1]))
            {
                Console.WriteLine(p);
            }
        }
    }
}
