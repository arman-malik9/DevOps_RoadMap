
import com.sun.net.httpserver.HttpServer;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

public class Main {

  public static void main(String[] args) throws IOException {
    // Create an instance of HttpServer bound to port defined by the 
    // PORT environment variable when present, otherwise on 8080.
    int port = Integer.parseInt(System.getenv().getOrDefault("PORT", "8080"));
    HttpServer server = HttpServer.create(new InetSocketAddress(port), 0);

    // Set root URI path.
    server.createContext("/", (var t) -> {
      byte[] response = "Hello World!".getBytes();
      t.sendResponseHeaders(200, response.length);
      try (OutputStream os = t.getResponseBody()) {
        os.write(response);
      }
    });

    // Create a second URI path.
    server.createContext("/foo", (var t) -> {
      byte[] response = "Foo!".getBytes();
      t.sendResponseHeaders(200, response.length);
      try (OutputStream os = t.getResponseBody()) {
        os.write(response);
      }
    });

    server.start();
  }
}