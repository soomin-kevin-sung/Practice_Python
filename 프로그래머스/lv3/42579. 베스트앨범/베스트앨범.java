import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        Map<String, Genre> map = new HashMap<>();
        
        for (int i = 0; i < genres.length; i++) {
            if (!map.containsKey(genres[i]))
                map.put(genres[i], new Genre(genres[i]));
            
            Genre genre = map.get(genres[i]);
            genre.addSong(i, plays[i]);
        }
        
        Genre[] sortedGenres = getSortedGenres(map);
        int[] answer = getBestAlbum(sortedGenres);
        
        return answer;
    }
    
    private int[] getBestAlbum(Genre[] genres) {
        ArrayList<Integer> list = new ArrayList<>();
        
        for (Genre genre : genres) {            
            list.add(genre.pollSong().index);
            if (genre.getNumberOfSongs() > 0)
                list.add(genre.pollSong().index);
        }
        
        int[] answer = new int[list.size()];
        for (int i = 0; i < answer.length; i++)
            answer[i] = list.get(i);
        
        return answer;
    }
    
    private Genre[] getSortedGenres(Map<String, Genre> map) {
        Genre[] answer = map.values().toArray(new Genre[0]);
        Arrays.sort(answer, (Genre a, Genre b) -> b.play - a.play);
        return answer;
    }
    
    class Song {
        public Song(int index, int play) {
            this.index = index;
            this.play = play;
        }
        
        int index;
        int play;
    }
    
    class Genre {
        public Genre(String name) {
            this.name = name;
            songs = new PriorityQueue<Song>((Song a, Song b) -> {
               if (a.play == b.play)
                   return a.index - b.index;
                
                return b.play - a.play;
            });
        }
        
        PriorityQueue<Song> songs;
        String name;
        int play;
        
        public void addSong(int index, int play) {
            songs.add(new Song(index, play));
            this.play += play;
        }
        
        public int getNumberOfSongs() {
            return songs.size();
        }
        
        public Song pollSong() {
            Song song = songs.poll();
            this.play -= song.play;
            return song;
        }
        
        @Override
        public int hashCode() {
            return name.hashCode();
        }
        
        @Override
        public String toString() {
            return "{name: " + name + ", play: " + play + "}";
        }
    }
}