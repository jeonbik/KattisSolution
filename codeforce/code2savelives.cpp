
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
 long long num,i,no_of_weapons,health,w1,w2;
 w1 = 0;
 w1 = 0;
 cin >> num;
// //  
// 	scanf("%d",&t);
// 	while(t--)
// 	{
// 		maxf=0;maxs=0;
// 		scanf("%d%d",&n,&h);
// 		while(n--)
// 		{
// 			scanf("%d",&a);
// 			if(a>=maxf)
// 			{
// 				maxs=maxf;
// 				maxf=a;
// 			}
// 			else if(a>maxs)
// 			{
// 				maxs=a;
// 			}
// 		}
// 		int ans=h/(maxf+maxs)*2;
// 		h=h%(maxs+maxf);
// 		if(h>maxf)ans+=2;
// 		else if(h)ans++;
// 		printf("%d\n",ans);
// 	}
 for (i = 0; i<num;i++){
      w1 = 0;
        w1 = 0;
     cin>> no_of_weapons>>health;
     while(no_of_weapons--){
         int damage;
         cin>>damage;
         if (damage >w1){
             w2 = w1;
             w1 = damage;
         }
         else if(damage > w2) w2 = damage;
     }

int hits  = health/(w1+w2)*2;
int remaining_health;
remaining_health = health%(w1+w2);
cout<<"Health "<<health<< " remaining health "<< remaining_health <<
" w1 "<< w1<< " w2 "<< w2<<" Hits "<<hits<<endl;
if (health < w1)cout<<1<<endl;
else if (remaining_health == 0)cout<<hits<<endl;
else if (remaining_health <= w1 && remaining_health != 0) cout<<(hits+1)<<endl;
else cout<<(hits+2)<<endl;

 }   

}

// 3
// 2 4
// 3 7
// 2 6
// 4 2
// 3 11
// 2 1 7

