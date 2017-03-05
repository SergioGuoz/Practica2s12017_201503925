/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package practica2edd;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;
import javax.swing.JFrame;

/**
 *
 * @author Sergio
 */
public class Practica2EDD {

    /**
     * @param args the command line arguments
     */
        public static void main(String[] args) {
        
           Inicio n=new Inicio();
           n.setVisible(true);
           n.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
           n.setLocationRelativeTo(null);
           
    }


}
