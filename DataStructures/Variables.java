import java.util.Arrays;

class Variables{
    public static void main(String[] args) {
        int a[] = {1,2,3,4,5,6};
        int b[] = new int[a.length-1];
        int index = 3;
        for (int i=0, k=0;i<a.length;i++) {
            if (i!= index){
                b[k++] = a[i];
            }
        }
        System.out.println("Array Before Deletion: "+ Arrays.toString(a));
        System.out.println("Array After Deletion: "+ Arrays.toString(b));
    }
}