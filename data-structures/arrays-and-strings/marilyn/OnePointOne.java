public class OnePointOne{
    public static boolean isUnique(String x){
        if(x.length() > 256){
            return false;
        }
        boolean[] chars = new boolean[256];
        for(int i = 0; i < x.length(); i++){
            char y = x.charAt(i);
            if(chars[(int)y]){
                return false;
            }
            chars[(int)y] = true;
        }
        return true;
    }

    public static void main(String[]args){
        //false
        System.out.println(isUnique("socorro"));
        //true
        System.out.println(isUnique("abcdefghij"));
    }
}
