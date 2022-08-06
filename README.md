O projeto foi desenvolvido utilizando a biblioteca Flask do Python, no qual se pode realizar o GET, POST, PUT ou DELETE de tarefas que possuem a seguinte estrutura:

  'id': int,  
  'responsavel': string,  
  'tarefa': string,  
  'status': string  
  
  ex:  
    
  'id': 0,  
  'responsavel': 'João',  
  'tarefa': 'Praticar Flask',  
  'status': 'Concluido'  
  
O ID das tarefas é gerado automaticamente quando relizado o POST, e a partir do mesmo é possível realizar consultadas, modificações ou exclusões.
