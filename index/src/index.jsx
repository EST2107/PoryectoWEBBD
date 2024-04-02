import "bootstrap/dist/css/bootstrap.min.css";
import NavbarComp from "./components/NavBarC";
import Container from "react-bootstrap/esm/Container";
import Row from "react-bootstrap/esm/Row";
import Col from "react-bootstrap/esm/Col";
import "./index.css";

export function IndexC() {
  return (
    <div className="cosita">
      <NavbarComp></NavbarComp>
      <Container>
        <Row>
          <Col></Col>
          <Col xs={6} className="Col">
            <p>
              La industria de servicios de alimentación ha experimentado una
              transformación significativa en los últimos años, impulsada en
              gran medida por la rápida adopción de tecnologías de información.
              En este contexto, "Delicias Dilcia", una comidería especializada
              en servicios de entrega a domicilio, se enfrenta al desafío de
              mantenerse competitiva y eficiente en un mercado dinámico y
              exigente.
            </p>
            <p>
              Previamente a la implementación de este proyecto, el propietario
              de "Delicias Dilcia" dependía en gran medida de métodos manuales
              para gestionar la información de los clientes. Anotar los datos en
              un cuaderno y posteriormente trasladarlos manualmente a hojas de
              cálculo de Excel constituía una práctica común. Este proceso,
              aunque tradicional, se mostró cada vez más insostenible frente a
              la creciente demanda y complejidad de las operaciones. El
              propietario experimentaba dificultades considerables, ya que esta
              metodología resultaba propensa a errores y consumía un tiempo
              valioso que podría dedicarse a otras tareas críticas del negocio.
            </p>
          </Col>
          <Col></Col>
        </Row>
      </Container>
      
    </div>
  );
}

export default NavbarComp;
