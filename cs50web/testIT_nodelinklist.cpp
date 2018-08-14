class Node
{
public:
    int value;
    Node *left;
    Node *right;

    //! This method returns a pointer to the node with the given​​​​​​​‌‌​​​‌​​‌​‌‌‌‌​‌​​​‌‌‌​‌ value.
    Node* find(int v){
        Node* temp = this;
        while(temp !=NULL)
        {
            if(temp->value == v)
                break;
            if(v> temp->value)
                temp = temp->right;
            else
            if(v< temp->value)
                temp = temp->left;
        }
        if (temp==NULL)
            return NULL;
        if (temp->value == v)
            return temp;
        return NULL;
    };
};

small->find(8)
large->find(0)


if (n==0)
    return 0;
if (n==1)
    return 1;
if (n==2)
    return -1;
int lstmove = -2;
int penmove = 1;
int lstpos = -1;

for (int i = 2; i<n; i++)
{
    int move = lstmove - penmove;
    lstpos = lstpos + move;
    penmove = lstmove;
    lstmove = move;
}
return lstpos;
