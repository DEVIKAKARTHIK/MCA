package CO1;

public class CPUprice {
    public static void main(String args[]) {
        cpu obj2 = new cpu();
        cpu.processor p = obj2.new processor();
        cpu.processor.ram obj1 = new cpu.processor.ram();
        System.out.println(obj2.price);
        System.out.println(p.core);        
        System.out.println(obj1.memory);        
    }
}

class cpu {
    int price = 100;
    
    class processor {
        int core = 5 ;
        String manufacturer = "devika";

        static class ram {
            String memory = "16GB";
            String manufacturer = "windows";
        }
    }
}
// create a class name cpu with attribute price create an inner class processor(no of cores, manufactureer) 
// and static nested class ram (attr memory , manufacturer)
// create an object of cpu and print informations of processor and ram