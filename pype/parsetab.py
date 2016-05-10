
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '7B77CFC2E9574BE6AA62E56690011F66'
    
_lr_action_items = {'OP_MUL':([14,],[20,]),'LPAREN':([0,1,2,3,7,8,9,11,12,13,15,16,18,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,52,53,54,55,57,58,],[6,6,-4,-5,-3,-2,14,-27,14,-28,-9,-26,-8,-7,14,14,36,14,14,14,36,-6,14,-30,14,36,-11,-17,-15,14,14,14,-21,14,36,-13,-24,-29,-25,-10,-14,-23,-20,-22,-12,-19,-16,]),'OUTPUT':([14,],[27,]),'LBRACE':([0,1,2,3,7,8,19,28,],[5,5,-4,-5,-3,-2,-7,-6,]),'IMPORT':([6,],[10,]),'STRING':([9,11,12,13,15,16,18,20,21,24,25,26,29,30,31,33,37,38,39,40,41,43,44,45,46,47,52,53,54,55,57,],[13,-27,13,-28,-9,-26,-8,13,13,13,13,13,13,-30,13,-11,13,13,13,-21,13,-13,-24,-29,-25,-10,-23,-20,-22,-12,-19,]),'NUMBER':([9,11,12,13,15,16,18,20,21,24,25,26,29,30,31,33,37,38,39,40,41,43,44,45,46,47,52,53,54,55,57,],[11,-27,11,-28,-9,-26,-8,11,11,11,11,11,11,-30,11,-11,11,11,11,-21,11,-13,-24,-29,-25,-10,-23,-20,-22,-12,-19,]),'RPAREN':([11,13,16,17,22,25,27,29,30,31,32,33,34,35,38,39,40,41,42,43,44,45,46,47,48,51,52,53,54,55,56,57,58,],[-27,-28,-26,28,33,40,43,44,-30,46,47,-11,-17,-15,52,53,-21,54,55,-13,-24,-29,-25,-10,-14,57,-23,-20,-22,-12,58,-19,-16,]),'OP_SUB':([14,],[24,]),'OP_ADD':([14,],[26,]),'ID':([5,9,10,11,12,13,14,15,16,18,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,55,57,58,],[9,16,17,-27,16,-28,25,-9,-26,-8,16,16,34,37,16,16,16,34,16,-30,16,34,-11,-17,-15,49,16,16,16,-21,16,34,-13,-24,-29,-25,-10,-14,-18,56,-23,-20,-22,-12,-19,-16,]),'ASSIGN':([14,],[23,]),'$end':([1,2,3,4,7,8,19,28,],[-1,-4,-5,0,-3,-2,-7,-6,]),'OP_DIV':([14,],[21,]),'RBRACE':([11,12,13,15,16,18,33,40,43,44,46,47,52,53,54,55,57,],[-27,19,-28,-9,-26,-8,-11,-21,-13,-24,-25,-10,-23,-20,-22,-12,-19,]),'INPUT':([14,],[22,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaration_list':([22,27,],[32,42,]),'statement_list':([0,],[1,]),'import_statement':([0,1,],[2,7,]),'expression':([9,12,20,21,24,25,26,29,31,37,38,39,41,],[15,18,30,30,30,30,30,45,45,51,45,45,45,]),'component':([0,1,],[3,8,]),'type':([36,],[50,]),'program':([0,],[4,]),'expression_list':([9,],[12,]),'declaration':([22,27,32,42,],[35,35,48,48,]),'parameter_list':([20,21,24,25,26,],[29,31,38,39,41,]),}

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
