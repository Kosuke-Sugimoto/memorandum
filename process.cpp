#include<iostream>
#include <sys/wait.h>
#include <unistd.h>

#define R (0) // 0が標準入力
#define W (1) // 1が標準出力

using namespace std;

int main(){
    char buffer[1024] = {};
    int _pipe[2];
    int pid, bytelen;

    if(pipe(_pipe) < 0){
        exit(EXIT_FAILURE);
    }
    
    pid = fork();

    if(pid < 0){
        // forkに失敗したならばパイプはどちらも閉じる
        close(_pipe[R]); close(_pipe[W]);
    }

    if(pid == 0){
        // 子プロセスでの処理
        // 読み取る必要はないので早々に読み取りパイプは閉じる
        close(_pipe[R]);
        // stdoutを書き込みパイプと繋げたら閉じる
        dup2(_pipe[W], W); close(_pipe[W]);
        char *const str[] = {"/bin/ls", "-l", NULL};
        execv("/bin/ls", str);
    }

    // 親プロセスでの処理
    // 書き込む必要はないので書き込みパイプは閉じる
    close(_pipe[W]);
    // パイプから読み込み
    int size = read(_pipe[R], buffer, 1024);
    cout << buffer << endl;
    string s(buffer);
    cout << s << endl;

    return 0;
}