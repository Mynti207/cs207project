
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '1D0986CF548090149FF07FC136CB2C82'
    
_lr_action_items = {'STRING':([9,11,12,13,14,15,18,20,21,23,24,26,29,30,31,36,37,38,39,40,41,43,44,45,46,50,51,52,54,55,57,],[11,-28,-27,-9,-26,11,-8,11,11,11,11,11,-30,11,11,-13,11,-21,11,11,11,-11,-29,-24,-22,-12,-23,-20,-25,-10,-19,]),'ASSIGN':([16,],[25,]),'IMPORT':([6,],[10,]),'OP_ADD':([16,],[21,]),'$end':([1,2,3,4,7,8,19,28,],[-4,-1,-5,0,-3,-2,-7,-6,]),'OP_SUB':([16,],[23,]),'LBRACE':([0,1,2,3,7,8,19,28,],[5,-4,5,-5,-3,-2,-7,-6,]),'NUMBER':([9,11,12,13,14,15,18,20,21,23,24,26,29,30,31,36,37,38,39,40,41,43,44,45,46,50,51,52,54,55,57,],[12,-28,-27,-9,-26,12,-8,12,12,12,12,12,-30,12,12,-13,12,-21,12,12,12,-11,-29,-24,-22,-12,-23,-20,-25,-10,-19,]),'OUTPUT':([16,],[22,]),'RPAREN':([11,12,14,17,22,24,27,29,30,31,32,33,35,36,37,38,39,41,42,43,44,45,46,49,50,51,52,53,54,55,56,57,58,],[-28,-27,-26,28,36,38,43,-30,45,46,-15,-17,50,-13,51,-21,52,54,55,-11,-29,-24,-22,-14,-12,-23,-20,57,-25,-10,58,-19,-16,]),'RBRACE':([11,12,13,14,15,18,36,38,43,45,46,50,51,52,54,55,57,],[-28,-27,-9,-26,19,-8,-13,-21,-11,-24,-22,-12,-23,-20,-25,-10,-19,]),'ID':([5,9,10,11,12,13,14,15,16,18,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,54,55,57,58,],[9,14,17,-28,-27,-9,-26,14,24,-8,14,14,33,14,14,40,14,33,-30,14,14,-15,-17,47,33,-13,14,-21,14,14,14,33,-11,-29,-24,-22,-18,56,-14,-12,-23,-20,-25,-10,-19,-16,]),'OP_MUL':([16,],[20,]),'OP_DIV':([16,],[26,]),'LPAREN':([0,1,2,3,7,8,9,11,12,13,14,15,18,19,20,21,22,23,24,26,27,28,29,30,31,32,33,35,36,37,38,39,40,41,42,43,44,45,46,49,50,51,52,54,55,57,58,],[6,-4,6,-5,-3,-2,16,-28,-27,-9,-26,16,-8,-7,16,16,34,16,16,16,34,-6,-30,16,16,-15,-17,34,-13,16,-21,16,16,16,34,-11,-29,-24,-22,-14,-12,-23,-20,-25,-10,-19,-16,]),'INPUT':([16,],[27,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'import_statement':([0,2,],[1,7,]),'parameter_list':([20,21,23,24,26,],[30,31,37,39,41,]),'declaration':([22,27,35,42,],[32,32,49,49,]),'type':([34,],[48,]),'expression_list':([9,],[15,]),'statement_list':([0,],[2,]),'component':([0,2,],[3,8,]),'program':([0,],[4,]),'expression':([9,15,20,21,23,24,26,30,31,37,39,40,41,],[13,18,29,29,29,29,29,44,44,44,44,53,44,]),'declaration_list':([22,27,],[35,42,]),}

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
