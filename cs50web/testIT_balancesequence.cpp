#include <string>
#include <stack>
using namespace std;

class Answer
{
public:
    //! checks that the given sequence is​​​​​​​‌‌​​​‌​​‌​‌‌‌‌​‌​​​‌‌‌​‌ correct
    static bool check(string sequence)
    {
        stack <char> s;
        char x;
        for (int i=0 ; i<sequence.length();i++)
        {
            if(sequence[i] =='(' || sequence[i]=='[')
            {
              //push
              s.push(sequence[i]);
              continue;
            }
            if (s.empty())
                return false;
            switch(sequence[i])
            {
            case ')':
                x= s.top();
                s.pop();
                if(x=='[')
                    return false;
                break;
            case ']':
                x=s.top();
                s.pop();
                if(x=='(')
                    return false;
                break;
            }
        }
        return (s.empty());
    }
};


cout << Answer::check("[(()])") << endl; // false

cout << Answer::check("([(([[(([]))]]))])") << endl;  // true
cout << Answer::check("[](()()[[]])()[]([])") << endl;// true
cout << Answer::check("([((([(([]))])))))])") << endl;// false
cout << Answer::check("[](()()[[]])[][[([])") << endl;// false
