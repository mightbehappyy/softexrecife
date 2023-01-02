package app;

import java.util.Date;
import javax.jws.WebService;

@WebService(endpointInterface = "app.Outro")
public class Servidor implements Outro{

    @Override
    public String pegarCpf(String cpfCliente) {
        return "o cpf do cliente e " + cpfCliente;
    }

    @Override
    public String criarCpf(String novoCpf) {
        return "o novo cpf e" + novoCpf;
    }

    @Override
    public String getNome(String nome) {
        return nome;
    }

    @Override
    public String setNome(String nome) {
        return "NOVO NOME:"+ nome;
    }

} 
