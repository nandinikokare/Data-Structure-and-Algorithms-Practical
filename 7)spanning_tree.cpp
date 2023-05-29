#include<iostream>
#include<string>
const int MAX=30;
using namespace std;
class Graph {
	int cities[MAX][MAX];
	string* map_array;
public:

	int getIndex(string city) {
		int i=1;
		while(map_array[i] != "\0") {
			if(map_array[i]==city) {
				return i;
			}
			i++;
		}
		i=1;
		while(map_array[i]!= "\0") {
			i++;
		}
		map_array[i]=city;
		return i;

	}

	string getCity(int index) {
		return map_array[index];
	}

	void create_graph(int n) {
		map_array=new string[n+1];

		string city,city1;
		int weight;
		int edges=(n*(n-1))/2; //maximum edges
		//initialize all with zero
		for(int i=1;i<=n;i++) {
			for(int j=1;j<=n;j++) {
				cities[i][j]=0;
			}
		}

		for(int i=1;i<=edges;i++) {
			cout<<"Enter data in form of (source city, destination city, weight)"<<endl;
			cin>>city>>city1>>weight;
			create_Matrix(city,city1,weight);
		}
	}

	void create_Matrix(string city,string city1,int weight) {
		int first = getIndex(city);
		int second = getIndex(city1);
		cities[first][second]=weight;
		cities[second][first]=weight;
	}

	int getCitiesCount() {
		int i=1;
		while(map_array[i] != "\0") {
			i++;
		}
		return i-1;
	}

	void traverse() {
		//cout<<"Count: "<<getCitiesCount()<<endl;
		cout<<"Adjacency matrix is: "<<endl;
		for(int i=1;i<=getCitiesCount();i++) {
			for(int j=1;j<=getCitiesCount();j++) {
				cout<<cities[i][j]<<"	";
			}
			cout<<endl;
		}
	}

	void kruskal() {
		cout<<"\nEdges in the minimum spanning tree are"<<endl;
		cout<<"Edges"<<"\t"<<"weight"<<endl;
		int father_array[getCitiesCount()+1]={0};
		int min=999;
		int weight=0;
		int count=0;
		int temp,temp1,t,t1,root_t,root_t1=0;
		while(count < getCitiesCount()-1) {
			min=999;
			for(int i=1;i<=getCitiesCount();i++) {
				for(int j=1;j<=getCitiesCount();j++) {
					if(min > cities[i][j] && cities[i][j] != 0) {
						min=cities[i][j];
						temp=i;
						temp1=j;
					}
				}
			}
			t=temp;
			t1=temp1;
			cities[temp][temp1]=cities[temp1][temp]=0;
			while(temp > 0) {
				root_t=temp;
				temp=father_array[temp];
			}
			while(temp1 > 0) {
				root_t1=temp1;
				temp1=father_array[temp1];
			}
			if(root_t != root_t1) {
				cout<<getCity(t)<<"--"<<getCity(t1)<<"\t"<<min<<endl;
				weight=weight+min;
				father_array[root_t1]=root_t;
				count++;
			}
		}
		cout<<"Total weight of the minimum spanning tree is: "<<weight<<endl;
	}

};

int main() {
	int n;
	Graph g;
	cout<<"How many nodes you want: ";
	cin>>n;
	g.create_graph(n);

/*	g.create_Matrix("m","p",5);
	g.create_Matrix("m","s",10);
	g.create_Matrix("m","a",9);
	g.create_Matrix("p","s",3);
	g.create_Matrix("p","a",2);
	g.create_Matrix("s","a",1);*/

	g.traverse();
	g.kruskal();
	return 0;
}
