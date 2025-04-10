from pydantic import BaseModel

# ---------- Respostas ----------
class AnswerCreate(BaseModel):
    texto: str
    correta: bool

# ---------- Perguntas ----------
class QuestionCreate(BaseModel):
    enunciado: str
    respostas: list[AnswerCreate]

# ---------- Quiz ----------
class QuizCreate(BaseModel):
    titulo: str
    conteudos: str
    perguntas: list[QuestionCreate]

# ---------- Sessão ----------
class CriarSessao(BaseModel):
    quiz_id: int

# ---------- Jogador entrando ----------
class EntrarPartida(BaseModel):
    nome: str
    pin: str

# ---------- Jogador respondendo ----------
class RespostaJogador(BaseModel):
    player_id: int
    resposta_id: int

class Responder(BaseModel):
    player_id: int
    question_id: int
    resposta_id: int
    pontuacao: int