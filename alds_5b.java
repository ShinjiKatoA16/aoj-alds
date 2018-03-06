import java.util.Scanner;
//import java.util.Arrays ;

// import java.InputMismatchException;
// alds_5b, Aizu Online Judge accept only class name: Main


class Main {

    public static int merge_count = 0 ;

    static void Merge(int [] A, int low, int mid, int high) {
        int l_size = mid-low ;
        int h_size = high-mid ;
        int []L = new int[l_size] ;
        int []H = new int[h_size] ;

        //System.out.printf("Merge: %d %d %d\n", low, mid, high) ;
        for (int i=0; i<l_size; i++) {
            L[i] = A[low+i] ;
        }
        for (int i=0; i<h_size; i++) {
            H[i] = A[mid+i] ;
        }

        int a_pos=low, l_pos=0, h_pos=0 ;

        while (l_size != 0 && h_size != 0) {
            if (L[l_pos] <= H[h_pos]) {
                A[a_pos] = L[l_pos] ;
                l_size -= 1 ;
                l_pos += 1 ;
            }
            else {
                A[a_pos] = H[h_pos] ;
                h_size -= 1 ;
                h_pos += 1 ;
            }
            a_pos += 1 ;
            merge_count++ ;
        }
        
        while (l_size != 0) {
            A[a_pos] = L[l_pos] ;
            l_size -= 1 ;
            l_pos += 1 ;
            a_pos += 1 ;
            merge_count++ ;
        }
        
        while (h_size != 0) {
            A[a_pos] = H[h_pos] ;
            h_size -= 1 ;
            h_pos += 1 ;
            a_pos += 1 ;
            merge_count++ ;
        }

    }

    static void Merge_sort(int [] A, int low, int high) {
        //System.out.printf("Merge_sort: %d %d\n", low, high) ;
        if (low + 1 < high) {
            int mid = (low + high) / 2 ;
            Merge_sort(A, low, mid) ;
            Merge_sort(A, mid, high) ;
            Merge(A, low, mid, high) ;
        }
    }

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in) ;
        String s = scanner.nextLine() ;

        int elem_count ;
        elem_count = Integer.parseInt(s) ;
        int A[] = new int[elem_count] ;

        for (int i=0; i<elem_count; i++) {
            A[i] = scanner.nextInt() ;
        }

        scanner.close() ;
        Merge_sort(A, 0, elem_count) ;

        for (int i=0; i<elem_count; i++) {
            String end_mark = " " ;
            if (i==elem_count-1) end_mark = "\n" ;
            System.out.print(A[i] + end_mark) ;
        }
        System.out.println(merge_count) ;
    }
}
