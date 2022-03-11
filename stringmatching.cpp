// while(True):
//     try:
//         to_find = input()
//         if not to_find:break
//         sentence = input()
//         # print(sentence)
//         if len (to_find) > len(sentence): pass
//         else:    
//             for i,char in enumerate(sentence):
//                 if char == to_find[0]:
//                     len_word = 0
//                     len_word = i + len(to_find)
//                     # print("Temp len: {} ".format(len_word))
//                     if len_word <= len(sentence): 
//                         # print("character: {} tofind: {} i: {} len of word: {}".format(char,to_find[0],i,len_word))
//                         word = sentence[i:len_word]
//                         # print("Word: ", word )
//                         if word == to_find: print(i,end = " ")
//             print("\n")
//     except:break

  #include <iostream>
    #include <string>
    using namespace std;

    int main(){
    string to_find,sentence;
    bool go = true;
    while (go){
        cin >> to_find;
        if (to_find.length() == 0) go = false;
        // cout<<"herhe"<<endl;
        cin >> sentence;
        if (to_find.length()>sentence.length()) 
        ;

    } 

    }