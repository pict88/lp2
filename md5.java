import java.security.MessageDigest;

public class MD5Blockchain {

    public static void main(String[] args) throws Exception {

        String previousHash = "0000";

        for (int block = 1; block <= 3; block++) {

            int nonce = 0;

            while (true) {

                String data = "Block" + block + previousHash + nonce;

                MessageDigest md = MessageDigest.getInstance("MD5");

                byte[] bytes = md.digest(data.getBytes());

                StringBuilder hash = new StringBuilder();

                for (byte b : bytes) {
                    hash.append(String.format("%02x", b));
                }

                // Proof of Work
                if (hash.toString().startsWith("00")) {

                    System.out.println("Block : " + block);
                    System.out.println("Previous Hash : " + previousHash);
                    System.out.println("Nonce : " + nonce);
                    System.out.println("Hash  : " + hash);

                    System.out.println();

                    previousHash = hash.toString();

                    break;
                }

                nonce++;
            }
        }
    }
}