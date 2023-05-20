#include<bits/stdc++.h>

using namespace std;

// bit全探索によって求めるnCr
// bit全探索を使うのでO(N*2^N)だと思われる
// O(2^N)の場合、N<=20で見積もるので今回のアルゴリズムではN<=15が関の山だと思われる
tuple<vector<vector<int>>, vector<vector<int>>> combination(vector<int> &target, int r){
    vector<vector<int>> result = {};
    vector<vector<int>> exclusive_result = {};
    for(int i=0;i<(1<<target.size());i++){
        vector<int> tmp = {};
        vector<int> ex_tmp = {};
        for(int j=0;j<target.size();j++){
            if(i&(1<<j)){
                tmp.push_back(target[j]);
            }else{
                ex_tmp.push_back(target[j]);
            }
        }
        if(tmp.size()==r){
            result.push_back(tmp);
            exclusive_result.push_back(ex_tmp);
        }
    }
    return make_tuple(result, exclusive_result);
}

int main(){
    vector<int> target = {2, 4, 6, 8, 10};
    tuple<vector<vector<int>>, vector<vector<int>>> pr = combination(target, 3);
    for(auto x : get<1>(pr)){
        for(auto y : x){
            cout << y << " ";
        }
        cout << endl;
    }
}