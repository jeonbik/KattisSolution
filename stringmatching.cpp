  #include <iostream>
    #include <string>
    using namespace std;

    int main(){
    string to_find,sentence;
    bool go = true;
    while (getline(cin,to_find)){
      if (to_find.length() == 0){break;}
        getline(cin,sentence);
        if (to_find.length()>sentence.length()) 
        ;
        else{
        for (int i = 0;i<sentence.length();i++){
          // cout<<"sentence[i] "<<sentence[i]<<" to_find[0] "<< to_find[0]<<endl;
          if (sentence[i] == to_find[0]){
            int len_word = i + to_find.length();
            // cout<<"Len_word "<<len_word<<endl;
              string word = sentence.substr(i,to_find.length());
              // cout<<"Word: "<<word<<" ";
              if (word == to_find) cout<<i<<" ";
            
          }
        }
        cout<<endl;
        }
    } 

    }

//     p
// Popup
// helo
// Hello there!
// peek a boo
// you speek a bootiful language
// anas
// bananananaspaj

