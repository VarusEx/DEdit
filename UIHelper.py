from PyQt5.QtWidgets import QAction, QMessageBox
from PyQt5.QtGui import QIcon

import FileHelper


def create_button(self, func_name, name_button, icon="", shortcut=""):
    icon_btn = FileHelper.get_image(icon)

    button = QAction(QIcon(icon_btn), name_button, self)
    button.setIcon(icon_btn)
    button.setShortcut(shortcut)
    button.triggered.connect(func_name)
    return button


npc_form = "instance TestNpc (Npc_Default)<br></bt>" \
           "{<br></bt>" \
           "name = \"TestNpc\";<br></bt>" \
           "guild = GIL_BAU; <br></bt>" \
           "id = 2137; <br></bt>" \
           "voice = 14; <br></bt>" \
           "flags = 0; <br></bt>" \
           "npctype = NPCTYPE_MAIN; <br></bt>" \
           "<br></bt>" \
           "B_SetAttributesToChapter(self, 2);<br></bt>" \
           "<br></bt>" \
           "fight_tactic = FAI_HUMAN_COWARD;<br></bt>" \
           "<br></bt>" \
           "B_CreateAmbientInv (self);<br></bt>" \
           "CreateInvItems		(self, ItMi_Hammer, 1);<br></bt>" \
           "<br></bt>" \
           "B_SetNpcVisual 		(self, MALE, \"Hum_Head_Bald\", Face_N_NormalBart03, BodyTex_N, ITAR_Bau_L);<br></bt>" \
           "Mdl_SetModelFatness	(self, 1);<br></bt>" \
           "Mdl_ApplyOverlayMds	(self, \"Humans_Relaxed.mds\");<br></bt>" \
           "<br></bt>" \
           "B_GiveNpcTalents (self);<br></bt>" \
           "<br></bt>" \
           "B_SetFightSkills (self, 20);<br></bt>" \
           "<br></bt>" \
           "daily_routine = Rtn_Start_2137;<br></bt>" \
           "};<br></bt>" \
           "<br></bt>" \
           "func void Rtn_Start_2137 ()<br></bt>" \
           "{<br></bt>" \
           "TA_Stand_Guarding	(08,00,23,00,\"Waypoint\"); " \
           "<br></bt>};"


dialog_form = "//############################################################\n" \
              "// 			  			EXIT\n" \
              "//############################################################\n" \
              "\n" \
              "instance DIA_NPC_EXIT(C_INFO)\n" \
              "{\n" \
              "npc            = NPC;\n" \
              "nr             = 999;\n" \
              "condition	  = DIA_NPC_EXIT_Condition;\n" \
              "information	  = DIA_NPC_EXIT_Info;\n" \
              "permanent	  = true;\n" \
              "description    = \"Koniec\";\n" \
              "};\n"
