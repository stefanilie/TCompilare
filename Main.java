/**
 *
 * @author Adrian
 */
package main;

import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

class Productie {

    String out1, out2;

    public Productie(String o1, String o2) {
        this.out1 = o1;
        this.out2 = o2;
    }
  
    public String toString(){
        return "(" + left + ", " + right + ")";
    }
}

class STOS {

    ArrayList<ArrayList<Productie>> Productii;
    ArrayList<String> Alfabet_in, Alfabet_out;
    String LAMBDA = "#", sir_format = "";
    int NETERMINALE;
    ArrayList<String> Output;
    ArrayList<String> prime_posibilitati;
    ArrayList<ArrayList<Pereche>> Productii_aplicate;
    String sir_intrare;
    int SIR_GASIT;

    public STOS(String filename) {
        try {
            Scanner sc = new Scanner(new java.io.File(filename));
            this.Productii = new ArrayList();
            this.Alfabet_in = new ArrayList();
            this.Alfabet_out = new ArrayList();
            this.Output = new ArrayList();
            this.prime_posibilitati = new ArrayList();
            this.Productii_aplicate = new ArrayList();
            this.NETERMINALE = sc.nextInt();
            this.SIR_GASIT = 0;
            int in, out, nr_prod;

            for (int i = 0; i < NETERMINALE; i++) {
                Productii.add(new ArrayList());
            }

            in = sc.nextInt();  //terminale intrare
            for (int i = 0; i < in; i++) {
                Alfabet_in.add(sc.next());
            }
            out = sc.nextInt();    //terminale iesire

            for (int i = 0; i < out; i++) {
                Alfabet_out.add(sc.next());
            }
            nr_prod = sc.nextInt();      //nr productiilor
            Productie p;
            int prod;
            for (int i = 0; i < nr_prod; i++) {
                prod = sc.nextInt();
                p = new Productie(sc.next(), sc.next());
                Productii.get(prod).add(p);
            }

        } catch (FileNotFoundException e) {
            System.out.println("File NOT found: " + e);
        }
    }
    
    /*
     returneaza sirul format din toate terminalele in ordinea
     in care apar
     */
    public String get_sir_terminale(String sir) {
        String s = "";
        int pos = 0;

        while (pos < sir.length()) {
            if (Alfabet_in.contains(sir.charAt(pos) + "")) {
                s += sir.charAt(pos);
            }
            pos++;
        }
        return s;
    }

    /*
        true : nu s-a depasit lungimea sirului dat la intrare
        false: in caz contrar 
     */
    public boolean continua(String s1, String s2) {
        return (s1.length() <= s2.length());
    }
    
    /*
        returneaza prefixul format din terminalele de la inceput
        (pana la primul neterminal)
    */
    public String get_prefix(String sir) {
        int pos = 0;
        String prefix = "";
        while (pos < sir.length()) {
            if (Alfabet_in.contains(sir.charAt(pos) + "")) {
                prefix += sir.charAt(pos);
            } else {
                break;
            }
            pos++;
        }
        return prefix;
    }

    /*
        se aplica productia cu simbolul de start S (sau 0) si
        se preiau primele siruri care posibil duc la sirul initial
        si se aplica productiile pe fiecare dintre acestea
     */
    public void start(String sir_in) {
        ArrayList<Productie> a = Productii.get(0);
        ArrayList<String> terminale_prefix = new ArrayList();
        String prefix;
        this.sir_intrare = sir_in.trim();

        for (int i = 0; i < a.size(); i++) {
            int pos = 0;
            Productie p = a.get(i);
            String out = p.out1;

            if (!out.equals(LAMBDA)) {
                prefix = get_prefix(out);
                if (sir_in.startsWith(prefix) && !prefix.isEmpty()) {
                    if (!terminale_prefix.contains(prefix)) {
                        terminale_prefix.add(prefix);
                    }
                    prime_posibilitati.add(out);
                    aplica_productii(out, "", i);
                }
            }
        }
        
        for (ArrayList<Pereche> ar: Productii_aplicate){
            System.out.println(ar);
        }
    }
    
    /*
        lista de productii care au condus la formarea cuvantului
    */
    public ArrayList<Pereche> get_productii(String sir_prod, int prod_in){
        sir_prod = "0" + prod_in + sir_prod;
        ArrayList<Pereche> ap = new ArrayList();
        for (int i = 0; i < sir_prod.length() - 1; i += 2){
            Pereche p = new Pereche(Integer.parseInt(sir_prod.charAt(i) + ""),
                                    Integer.parseInt(sir_prod.charAt(i + 1) + ""));
            ap.add(p);
        }
        return ap;
    }
    
    /*
        primul neterminal din sirul dat ca parametru
    */
    public String primul_neterminal(String sir) {
        int pos = 0;
        String n = "";
        while (pos < sir.length()) {
            if (!Alfabet_in.contains(sir.charAt(pos) + "")) {
                n = sir.charAt(pos) + ""; 
                break;
            }
            pos++;
        }
        return n;
    }
    
    /*
        se aplica recursiv toate productiile posibile pentru sirul
        dat ca parametru (input)
    */
    public void aplica_productii(String input, String sir_productii, int prod_in) {
       // System.out.println(input);
        if (input.trim().equals(this.sir_intrare)) { //am ajuns la sirul dorit
            SIR_GASIT = 1;
            sir_format = input;
            //System.out.println(sir_productii);
            Productii_aplicate.add(get_productii(sir_productii, prod_in));
        } else if (continua(get_sir_terminale(input), sir_intrare)) {
            String neterm = primul_neterminal(input);
            if (neterm.isEmpty()) {
                return;
            }

            int netr = Integer.parseInt(neterm);
            ArrayList<Productie> a = Productii.get(netr);

            for (int i = 0; i < a.size(); i++) {
                Productie p = a.get(i);
                String out = (p.out1.equals(LAMBDA)) ? "" : p.out1;
                String sir_nou = input.replaceFirst(neterm, out); //se aplica productia
                String pref = get_prefix(sir_nou);
                if (sir_intrare.startsWith(pref.trim())) { //daca se formeaza sirul corect
                    String s_p = sir_productii + neterm + i;
                    aplica_productii(sir_nou, s_p, prod_in); //continua cu noul sir format
                }
            }
        }
    } //end of function
    
    /*
        se formeaza toate sirurile corespunzatoare sirului dat la intrare
    */
    public void get_siruri_iesire(){
        String sir_iesire;
        String prod_nr, sir_prod;
        
        for (ArrayList<Pereche> ap: Productii_aplicate){
            sir_iesire = Productii.get(ap.get(0).left).get(ap.get(0).right).out2;
            for (int i = 1; i < ap.size(); i++){
                prod_nr = ap.get(i).left + "";
                sir_prod = Productii.get(ap.get(i).left).get(ap.get(i).right).out2;
                sir_prod = (sir_prod.equals(LAMBDA)) ? "" : sir_prod;
                sir_iesire = sir_iesire.replaceFirst(prod_nr, sir_prod);
            }
            if (!Output.contains(sir_iesire)){
                Output.add(sir_iesire);
            }
        }
        
        //System.out.println(Output);
        for (String s: Output){
            s = s.replaceAll("x", "1");
            s = s.replaceAll("y", "2");
            s = s.replaceAll("z", "3");
            System.out.print(s + " ");
        }
        //System.out.println(Output);
    }// end of function
    
}

public class Main {

    public static void main(String[] args) {
        STOS schema = new STOS("sourceSTOS4.txt");

        schema.start("baba");
        //System.out.println(schema.sir_format);
        schema.get_siruri_iesire();
    }
}
