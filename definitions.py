from pydantic import BaseModel

class Report(BaseModel):
  hdr: str
  imei: str
  cmd_atualizacao: str
  gps_ligado_desligado: str
  data_hex: str
  hora_hex: str
  lat_hex: float
  lng_hex: float
  velocidade_hex: str
  direcao_hex: str
  status: str
  sinal: str
  bat_interna: str
  combustivel: str
  hodmetro_hex: str
  altitude: str
  dados_GPS: str
  RDFI: str
  temperatura: str
  bat_externa: str
  qtd_satelites: str
  date_report: str