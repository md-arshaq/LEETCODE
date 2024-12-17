class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        max_dur = events[0][1]
        max_index = events[0][0]

        for i in range(1,len(events)):
            duration =events[i][1] - events[i-1][1]

            if duration>max_dur or (duration == max_dur and events[i][0] < max_index):
                max_dur = duration
                max_index = events[i][0]
            
        return max_index