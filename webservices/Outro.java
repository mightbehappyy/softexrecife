package app;


import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.soap.SOAPBinding;
import javax.jws.soap.SOAPBinding.Style;
import javax.xml.ws.WebEndpoint;

@WebService
@SOAPBinding(style = Style.RPC)
public interface Outro{
    @WebMethod String pegarCpf(String cpfCliente);
    @WebMethod String criarCpf(String novoCpf);
    @WebMethod String getNome(String nome);
    @WebMethod String setNome(String nome);


}