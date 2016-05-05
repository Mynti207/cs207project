
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '6A65CD8BFBEB79DCE9C7C577BDAF4664'
    
_lr_action_items = {'OP_MUL':([12,],[19,]),'OP_ADD':([12,],[20,]),'NUMBER':([10,13,14,15,16,17,19,20,21,22,26,28,29,30,31,32,33,34,37,40,41,43,44,45,46,47,48,49,54,55,57,],[13,-27,-28,-26,13,-9,13,13,13,13,13,-8,13,-30,13,13,13,-21,-13,13,-11,13,-24,-29,-22,-23,-20,-12,-10,-25,-19,]),'OP_SUB':([12,],[21,]),'STRING':([10,13,14,15,16,17,19,20,21,22,26,28,29,30,31,32,33,34,37,40,41,43,44,45,46,47,48,49,54,55,57,],[14,-27,-28,-26,14,-9,14,14,14,14,14,-8,14,-30,14,14,14,-21,-13,14,-11,14,-24,-29,-22,-23,-20,-12,-10,-25,-19,]),'RBRACE':([13,14,15,16,17,28,34,37,41,44,46,47,48,49,54,55,57,],[-27,-28,-26,27,-9,-8,-21,-13,-11,-24,-22,-23,-20,-12,-10,-25,-19,]),'INPUT':([12,],[25,]),'ID':([6,7,10,12,13,14,15,16,17,19,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,54,55,57,58,],[10,11,15,22,-27,-28,-26,15,-9,15,15,15,15,36,40,36,15,-8,15,-30,15,15,15,-21,36,-17,-13,-15,52,15,-11,36,15,-24,-29,-22,-23,-20,-12,-14,56,-18,-10,-25,-19,-16,]),'LBRACE':([0,1,2,4,8,9,18,27,],[6,-5,-4,6,-2,-3,-6,-7,]),'OUTPUT':([12,],[23,]),'RPAREN':([11,13,14,15,22,23,25,29,30,31,32,33,34,35,36,37,38,41,42,43,44,45,46,47,48,49,50,53,54,55,56,57,58,],[18,-27,-28,-26,34,37,41,44,-30,46,47,48,-21,49,-17,-13,-15,-11,54,55,-24,-29,-22,-23,-20,-12,-14,57,-10,-25,58,-19,-16,]),'ASSIGN':([12,],[24,]),'LPAREN':([0,1,2,4,8,9,10,13,14,15,16,17,18,19,20,21,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,54,55,57,58,],[3,-5,-4,3,-2,-3,12,-27,-28,-26,12,-9,-6,12,12,12,12,39,39,12,-7,-8,12,-30,12,12,12,-21,39,-17,-13,-15,12,-11,39,12,-24,-29,-22,-23,-20,-12,-14,-10,-25,-19,-16,]),'IMPORT':([3,],[7,]),'OP_DIV':([12,],[26,]),'$end':([1,2,4,5,8,9,18,27,],[-5,-4,-1,0,-2,-3,-6,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'component':([0,4,],[1,8,]),'import_statement':([0,4,],[2,9,]),'parameter_list':([19,20,21,22,26,],[29,31,32,33,43,]),'declaration_list':([23,25,],[35,42,]),'statement_list':([0,],[4,]),'program':([0,],[5,]),'declaration':([23,25,35,42,],[38,38,50,50,]),'expression_list':([10,],[16,]),'type':([39,],[51,]),'expression':([10,16,19,20,21,22,26,29,31,32,33,40,43,],[17,28,30,30,30,30,30,45,45,45,45,53,45,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','parser.py',20),
  ('statement_list -> statement_list component','statement_list',2,'p_statement_list','parser.py',26),
  ('statement_list -> statement_list import_statement','statement_list',2,'p_statement_list','parser.py',27),
  ('statement_list -> import_statement','statement_list',1,'p_statement_list','parser.py',28),
  ('statement_list -> component','statement_list',1,'p_statement_list','parser.py',29),
  ('import_statement -> LPAREN IMPORT ID RPAREN','import_statement',4,'p_import_statement','parser.py',38),
  ('component -> LBRACE ID expression_list RBRACE','component',4,'p_component','parser.py',43),
  ('expression_list -> expression_list expression','expression_list',2,'p_expression_list','parser.py',49),
  ('expression_list -> expression','expression_list',1,'p_expression_list','parser.py',50),
  ('expression -> LPAREN INPUT declaration_list RPAREN','expression',4,'p_inputexpression','parser.py',59),
  ('expression -> LPAREN INPUT RPAREN','expression',3,'p_inputexpression','parser.py',60),
  ('expression -> LPAREN OUTPUT declaration_list RPAREN','expression',4,'p_outputexpression','parser.py',68),
  ('expression -> LPAREN OUTPUT RPAREN','expression',3,'p_outputexpression','parser.py',69),
  ('declaration_list -> declaration_list declaration','declaration_list',2,'p_declaration_list','parser.py',77),
  ('declaration_list -> declaration','declaration_list',1,'p_declaration_list','parser.py',78),
  ('declaration -> LPAREN type ID RPAREN','declaration',4,'p_declaration','parser.py',87),
  ('declaration -> ID','declaration',1,'p_declaration','parser.py',88),
  ('type -> ID','type',1,'p_type','parser.py',97),
  ('expression -> LPAREN ASSIGN ID expression RPAREN','expression',5,'p_expression_assign','parser.py',103),
  ('expression -> LPAREN ID parameter_list RPAREN','expression',4,'p_expression_id_parens','parser.py',108),
  ('expression -> LPAREN ID RPAREN','expression',3,'p_expression_id_parens','parser.py',109),
  ('expression -> LPAREN OP_ADD parameter_list RPAREN','expression',4,'p_op_add_expression','parser.py',118),
  ('expression -> LPAREN OP_SUB parameter_list RPAREN','expression',4,'p_op_sub_expression','parser.py',125),
  ('expression -> LPAREN OP_MUL parameter_list RPAREN','expression',4,'p_op_mul_expression','parser.py',132),
  ('expression -> LPAREN OP_DIV parameter_list RPAREN','expression',4,'p_op_div_expression','parser.py',139),
  ('expression -> ID','expression',1,'p_expression_id','parser.py',145),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',150),
  ('expression -> STRING','expression',1,'p_expression_string','parser.py',155),
  ('parameter_list -> parameter_list expression','parameter_list',2,'p_parameter_list','parser.py',160),
  ('parameter_list -> expression','parameter_list',1,'p_parameter_list','parser.py',161),
]
