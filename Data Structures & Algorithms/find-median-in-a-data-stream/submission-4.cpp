class MedianFinder {
    priority_queue<int,vector<int>,less<int>> smallHeap;
    priority_queue<int,vector<int>,greater<int>> largeHeap;
public:
    MedianFinder() {}
    
    void addNum(int num) {
        smallHeap.push(num);
        if(!largeHeap.empty() && smallHeap.top()>largeHeap.top()){
            largeHeap.push(smallHeap.top());
            smallHeap.pop();
        }

        if(largeHeap.size()>smallHeap.size()){
            smallHeap.push(largeHeap.top());
            largeHeap.pop();
        }
        else if(largeHeap.size()<smallHeap.size()){
            largeHeap.push(smallHeap.top());
            smallHeap.pop();
        }
    }
    double findMedian() {
        if(largeHeap.size()>smallHeap.size()){
            return largeHeap.top();
        }
        else if(largeHeap.size()<smallHeap.size()){
            return smallHeap.top();
        }
        else{
            return (largeHeap.top()+smallHeap.top())/2.0;
        }
    }
};
