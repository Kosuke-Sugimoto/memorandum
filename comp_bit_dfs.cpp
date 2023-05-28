#include<bits/stdc++.h>

using namespace std;

// 型の簡略化
// int64_tは多くの場合long longと同じ
// int64_tは64bit固定、long longは64bit以上という違い
using ll=long long;
using vi=vector<int>;
using vvi=vector<vector<int>>;
using vll=vector<ll>;
using vvll=vector<vector<ll>>;
using vs=vector<string>;

// マクロ定義
#define rep(i, n) for(int i=0; i<(int)(n); i++)
#define rep2(i, st, ed) for(int i=(int)(st); i<(int)(ed); i++)
#define repv(i, v) for(auto i : v)
#define all(v) (v).begin(),(v).end()

int MAX = 3;

// dfs再帰関数
void dfs(string now){
    if(now.size()==MAX) cout << now << endl;
    else{
        rep(i, 2){
            string next = now + to_string(i);
            dfs(next);
        }
    }
}

int main(){
    int n = 3;
    
    cout << "================ bit ================" << endl;

    rep(i, 1<<n){
        // rep(i, n)にしてもよいが、その場合には
        // 先に処理した方(数字が小さいほうが)先に出力されることに注意
        for(int j=n-1;j>=0;j--){
            if(i & 1<<j) cout << "1";
            else cout << "0";
        }
        cout << endl;
    }

    cout << "=====================================" << endl;

    cout << "================ rec ================" << endl;

    dfs("");

    cout << "=====================================" << endl;

    cout << "=============== stack ===============" << endl;

    stack<string> st;
    st.push("");

    string now, next;
    while(!st.empty()){
        now = st.top();
        st.pop();
        if(now.size()==3) cout << now << endl;
        else{
            for(int i=1;i>=0;i--){
                next = now + to_string(i);
                st.push(next);
            }
        }
    }

    cout << "=====================================" << endl;
}