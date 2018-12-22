public class Q2 {
    //单例模式
    //延迟加载，多线程可用
    private static volatile Object instance;

    private Q2(){}

    public static Object getInstance() {
        if (instance == null){
            synchronized (Q2.class){
                if (instance == null){
                    instance = new Q2();
                }
            }
        }
        return instance;
    }
}