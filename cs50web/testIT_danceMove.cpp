class Kariakoo
{
public:
    /** @return the position of the Kariakoo dancer at stage n​​​​​​​‌‌​​​‌​​‌​‌‌‌‌​‌​​​‌‌‌​‌ */
    static int getPositionAt(int n)
    {
        int ls[] ={0,1,-1,-4,-4,-3};
        return ls[n%6];
    }
};

cout << Kariakoo::getPositionAt(3) << endl; // -4
cout << Kariakoo::getPositionAt(100000) << endl; // -5
cout << Kariakoo::getPositionAt(2147483647) << endl; // 1
cout << Kariakoo::getPositionAt(5) << endl;
cout << Kariakoo::getPositionAt(6) << endl;
