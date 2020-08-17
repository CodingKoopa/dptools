#!/usr/bin/env python3

import argparse
import re
import sys

# Exported from /include/gflib/strcode.h.
# Find: ^(?:(?=[^\r\n])\s)([^\s]+) = [\dxabcdef]+,\s*\/\/\s*"*([^"\r\n]+)"*$
# Replace: "$1": "$2",
strcode = {
    "spc_": "　",
    "aa_": "ぁ",
    "a_": "あ",
    "ii_": "ぃ",
    "i_": "い",
    "uu_": "ぅ",
    "u_": "う",
    "ee_": "ぇ",
    "e_": "え",
    "oo_": "ぉ",
    "o_": "お",
    "ka_": "か",
    "ga_": "が",
    "ki_": "き",
    "gi_": "ぎ",
    "ku_": "く",
    "gu_": "ぐ",
    "ke_": "け",
    "ge_": "げ",
    "ko_": "こ",
    "go_": "ご",
    "sa_": "さ",
    "za_": "ざ",
    "si_": "し",
    "zi_": "じ",
    "su_": "す",
    "zu_": "ず",
    "se_": "せ",
    "ze_": "ぜ",
    "so_": "そ",
    "zo_": "ぞ",
    "ta_": "た",
    "da_": "だ",
    "ti_": "ち",
    "di_": "ぢ",
    "ttu_": "っ",
    "tu_": "つ",
    "du_": "づ",
    "te_": "て",
    "de_": "で",
    "to_": "と",
    "do_": "ど",
    "na_": "な",
    "ni_": "に",
    "nu_": "ぬ",
    "ne_": "ね",
    "no_": "の",
    "ha_": "は",
    "ba_": "ば",
    "pa_": "ぱ",
    "hi_": "ひ",
    "bi_": "び",
    "pi_": "ぴ",
    "hu_": "ふ",
    "bu_": "ぶ",
    "pu_": "ぷ",
    "he_": "へ",
    "be_": "べ",
    "pe_": "ぺ",
    "ho_": "ほ",
    "bo_": "ぼ",
    "po_": "ぽ",
    "ma_": "ま",
    "mi_": "み",
    "mu_": "む",
    "me_": "め",
    "mo_": "も",
    "yya_": "ゃ",
    "ya_": "や",
    "yyu_": "ゅ",
    "yu_": "ゆ",
    "yyo_": "ょ",
    "yo_": "よ",
    "ra_": "ら",
    "ri_": "り",
    "ru_": "る",
    "re_": "れ",
    "ro_": "ろ",
    "wa_": "わ",
    "wo_": "を",
    "n_": "ん",
    "AA_": "ァ",
    "A_": "ア",
    "II_": "ィ",
    "I_": "イ",
    "UU_": "ゥ",
    "U_": "ウ",
    "EE_": "ェ",
    "E_": "エ",
    "OO_": "ォ",
    "O_": "オ",
    "KA_": "カ",
    "GA_": "ガ",
    "KI_": "キ",
    "GI_": "ギ",
    "KU_": "ク",
    "GU_": "グ",
    "KE_": "ケ",
    "GE_": "ゲ",
    "KO_": "コ",
    "GO_": "ゴ",
    "SA_": "サ",
    "ZA_": "ザ",
    "SI_": "シ",
    "ZI_": "ジ",
    "SU_": "ス",
    "ZU_": "ズ",
    "SE_": "セ",
    "ZE_": "ゼ",
    "SO_": "ソ",
    "ZO_": "ゾ",
    "TA_": "タ",
    "DA_": "ダ",
    "TI_": "チ",
    "DI_": "ヂ",
    "TTU_": "ッ",
    "TU_": "ツ",
    "DU_": "ヅ",
    "TE_": "テ",
    "DE_": "デ",
    "TO_": "ト",
    "DO_": "ド",
    "NA_": "ナ",
    "NI_": "ニ",
    "NU_": "ヌ",
    "NE_": "ネ",
    "NO_": "ノ",
    "HA_": "ハ",
    "BA_": "バ",
    "PA_": "パ",
    "HI_": "ヒ",
    "BI_": "ビ",
    "PI_": "ピ",
    "HU_": "フ",
    "BU_": "ブ",
    "PU_": "プ",
    "HE_": "ヘ",
    "BE_": "ベ",
    "PE_": "ペ",
    "HO_": "ホ",
    "BO_": "ボ",
    "PO_": "ポ",
    "MA_": "マ",
    "MI_": "ミ",
    "MU_": "ム",
    "ME_": "メ",
    "MO_": "モ",
    "YYA_": "ャ",
    "YA_": "ヤ",
    "YYU_": "ュ",
    "YU_": "ユ",
    "YYO_": "ョ",
    "YO_": "ヨ",
    "RA_": "ラ",
    "RI_": "リ",
    "RU_": "ル",
    "RE_": "レ",
    "RO_": "ロ",
    "WA_": "ワ",
    "WO_": "ヲ",
    "N_": "ン",
    "n0_": "０",
    "n1_": "１",
    "n2_": "２",
    "n3_": "３",
    "n4_": "４",
    "n5_": "５",
    "n6_": "６",
    "n7_": "７",
    "n8_": "８",
    "n9_": "９",
    "A__": "Ａ",
    "B__": "Ｂ",
    "C__": "Ｃ",
    "D__": "Ｄ",
    "E__": "Ｅ",
    "F__": "Ｆ",
    "G__": "Ｇ",
    "H__": "Ｈ",
    "I__": "Ｉ",
    "J__": "Ｊ",
    "K__": "Ｋ",
    "L__": "Ｌ",
    "M__": "Ｍ",
    "N__": "Ｎ",
    "O__": "Ｏ",
    "P__": "Ｐ",
    "Q__": "Ｑ",
    "R__": "Ｒ",
    "S__": "Ｓ",
    "T__": "Ｔ",
    "U__": "Ｕ",
    "V__": "Ｖ",
    "W__": "Ｗ",
    "X__": "Ｘ",
    "Y__": "Ｙ",
    "Z__": "Ｚ",
    "a__": "ａ",
    "b__": "ｂ",
    "c__": "ｃ",
    "d__": "ｄ",
    "e__": "ｅ",
    "f__": "ｆ",
    "g__": "ｇ",
    "h__": "ｈ",
    "i__": "ｉ",
    "j__": "ｊ",
    "k__": "ｋ",
    "l__": "ｌ",
    "m__": "ｍ",
    "n__": "ｎ",
    "o__": "ｏ",
    "p__": "ｐ",
    "q__": "ｑ",
    "r__": "ｒ",
    "s__": "ｓ",
    "t__": "ｔ",
    "u__": "ｕ",
    "v__": "ｖ",
    "w__": "ｗ",
    "x__": "ｘ",
    "y__": "ｙ",
    "z__": "ｚ",
    "Plus__": "＋",
    "comma_": "，",
    "bou_": "ー",
    "period_": "．",
    "sura_": "／",
    "MaruKako__": "（",
    "MaruKakot__": "）",
    "colon_": "：",
    "semicolon_": "；",
    "gyoe_": "！",
    "hate_": "？",
    "us_quote1d_": "英語全角引用符（閉じ）／アポストロフィー",
    "us_quote2_": "英語全角２重引用符（開き）／独語２重引用符（閉じ）",
    "us_quote2d_": "英語全角２重引用符（閉じ）",
    "kako_": "「",
    "kakot_": "」",
    "kako2_": "『",
    "kakot2_": "』",
    "ten_": "、",
    "kten_": "。",
    "tenten_": "…",
    "h_spc_": " ",
    "h_n0_": "0",
    "h_n1_": "1",
    "h_n2_": "2",
    "h_n3_": "3",
    "h_n4_": "4",
    "h_n5_": "5",
    "h_n6_": "6",
    "h_n7_": "7",
    "h_n8_": "8",
    "h_n9_": "9",
    "h_A__": "A",
    "h_B__": "B",
    "h_C__": "C",
    "h_D__": "D",
    "h_E__": "E",
    "h_F__": "F",
    "h_G__": "G",
    "h_H__": "H",
    "h_I__": "I",
    "h_J__": "J",
    "h_K__": "K",
    "h_L__": "L",
    "h_M__": "M",
    "h_N__": "N",
    "h_O__": "O",
    "h_P__": "P",
    "h_Q__": "Q",
    "h_R__": "R",
    "h_S__": "S",
    "h_T__": "T",
    "h_U__": "U",
    "h_V__": "V",
    "h_W__": "W",
    "h_X__": "X",
    "h_Y__": "Y",
    "h_Z__": "Z",
    "h_a__": "a",
    "h_b__": "b",
    "h_c__": "c",
    "h_d__": "d",
    "h_e__": "e",
    "h_f__": "f",
    "h_g__": "g",
    "h_h__": "h",
    "h_i__": "i",
    "h_j__": "j",
    "h_k__": "k",
    "h_l__": "l",
    "h_m__": "m",
    "h_n__": "n",
    "h_o__": "o",
    "h_p__": "p",
    "h_q__": "q",
    "h_r__": "r",
    "h_s__": "s",
    "h_t__": "t",
    "h_u__": "u",
    "h_v__": "v",
    "h_w__": "w",
    "h_x__": "x",
    "h_y__": "y",
    "h_z__": "z",
    "h_plus_": "+",
    "h_comma_": ",",
    "h_bou_": "-",
    "h_period_": ".",
    "h_sura_": "/",
    "h_MaruKako__": "(",
    "h_MaruKakot__": ")",
    "h_colon_": ":",
    "h_semicolon_": ";",
    "h_gyoe_": "!",
    "h_hate_": "?",
    "us_h_quote1_": "英語半角引用符／アポストロフィー",
    "us_h_quote2_": "英語半角２重引用符",
    "osu_": "♂",
    "mesu_": "♀",
    "Agrave_": "Aアクサングラーブ ",
    "Aacute_": "Aアクサンテギュ ",
    "Acirc_": "Aサーカムフレックス ",
    "Atilde_": "Aティルド ",
    "Auml_": "Aウムラウト ",
    "Aring_": "Aリング ",
    "AElig_": "AE合字 ",
    "Ccedil_": "Cセディラ ",
    "Egrave_": "Eアクサングラーブ ",
    "Eacute_": "Eアクサンテギュ ",
    "Ecirc_": "Eサーカムフレックス ",
    "Euml_": "Eウムラウト ",
    "Igrave_": "Iアクサングラーブ ",
    "Iacute_": "Iアクサンテギュ ",
    "Icirc_": "Iサーカムフレックス ",
    "Iuml_": "Iウムラウト ",
    "ETH_": "音声記号eth ",
    "Ntilde_": "Nティルド ",
    "Ograve_": "Oアクサングラーブ ",
    "Oacute_": "Oアクサンテギュ ",
    "Ocirc_": "Oサーカムフレックス ",
    "Otilde_": "Oティルド ",
    "Ouml_": "Oウムラウト ",
    "times_": "×",
    "Oslash_": "Oスラッシュ ",
    "Ugrave_": "Uアクサングラーブ ",
    "Uacute_": "Uアクサンテギュ ",
    "Ucirc_": "Uサーカムフレックス ",
    "Uuml_": "Uウムラウト ",
    "Yacute_": "Yアクサンテギュ ",
    "THORN_": "音声記号th ",
    "szlig_": "sz合字 ",
    "agrave_": "aアクサングラーブ ",
    "aacute_": "aアクサンテギュ ",
    "acirc_": "aサーカムフレックス ",
    "atiled_": "aティルド ",
    "auml_": "aウムラウト ",
    "aring_": "aリング ",
    "aelig_": "ae合字 ",
    "ccedil_": "cセディラ ",
    "egrave_": "eアクサングラーブ ",
    "eacute_": "eアクサンテギュ ",
    "ecirc_": "eサーカムフレックス ",
    "euml_": "eウムラウト ",
    "igrave_": "iアクサングラーブ ",
    "iacute_": "iアクサンテギュ ",
    "icirc_": "iサーカムフレックス ",
    "iuml_": "iウムラウト ",
    "eth_": "eth合字 ",
    "ntiled_": "nティルド ",
    "ograve_": "oアクサングラーブ ",
    "oacute_": "oアクサンテギュ ",
    "ocirc_": "oサーカムフレックス ",
    "otilde_": "oティルド ",
    "ouml_": "oウムラウト ",
    "divide_": "÷",
    "oslash_": "oスラッシュ ",
    "ugrave_": "uアクサングラーブ ",
    "uacute_": "uアクサンテギュ ",
    "ucirc_": "uサーカムフレックス ",
    "uuml_": "uウムラウト ",
    "yacute_": "yアクサンテギュ ",
    "thorn_": "音声記号th ",
    "yuml_": "yウムラウト ",
    "OElig_": "OE合字 ",
    "oelig_": "oe合字 ",
    "Scedil_": "Sセディラ ",
    "scedil_": "sセディラ ",
    "rgyoe_": "反転！",
    "rhate_": "反転？",
    "MARU1__": "マル数字１",
    "MARU2__": "マル数字２",
    "MARU3__": "マル数字３",
    "MARU4__": "マル数字４",
    "MARU5__": "マル数字５",
    "MARU6__": "マル数字６",
    "MARU7__": "マル数字７",
    "MARU8__": "マル数字８",
    "MARU9__": "マル数字９",
    "ArrowL__": "←",
    "ArrowU__": "↑",
    "ArrowR__": "→",
    "ArrowD__": "↓",
    "yen_": "円",
    "pokedoru_": "ポケドル",
    "pocket_item": "ポケットアイコン：どうぐ",
    "pocket_keyitem": "ポケットアイコン：だいじなもの",
    "pocket_wazamachine": "ポケットアイコン：わざマシン",
    "pocket_seal": "ポケットアイコン：シール",
    "pocket_medicine": "ポケットアイコン：くすり",
    "pocket_nut": "ポケットアイコン：きのみ",
    "pocket_ball": "ポケットアイコン：モンスターボール",
    "pocket_battle": "ポケットアイコン：戦闘用",
    "h_osu_": "<",
    "h_mesu_": ">",
    "equal_": "＝",
    "h_equal_": "=",
    "nakag_": "・",
    "h_nakag_": "･",
    "wave_": "?",
    "spade_": "トランプのスペード",
    "club_": "トランプのクラブ",
    "heart_": "トランプのハート",
    "diamond_": "トランプのダイヤ",
    "star_": "星形",
    "double_circle_": "◎",
    "circle_": "○",
    "square_": "□",
    "triangle_": "△",
    "lozenge__": "◇",
    "atmark_": "＠",
    "note_": "♪",
    "percent_": "％",
    "h_percent_": "%",
    "sun_": "晴れマーク",
    "cloud_": "くもりマーク",
    "rain_": "雨マーク",
    "snow_": "雪マーク",
    "org_face_normal_": "顔マーク：すまし",
    "org_face_smile_": "顔マーク：えがお",
    "org_face_cry_": "顔マーク：泣き",
    "org_face_angry_": "顔マーク：怒り",
    "org_upper_": "上カーブやじるし",
    "org_downer_": "下カーブやじるし",
    "org_sleep_": "熟睡マーク",
    "cursor_": "カーソル",
    "charcode_reserve3_": "■",
    "charcode_reserve1_": "▼",
    "charcode_reserve2_": "▽",
}

strcode_reverse = dict(map(reversed, strcode.items()))


def encode(args):
  text = args.text
  if args.array_name:
    encoded_arr = "static const u16 {}[]  = {{".format(args.array_name)
  else:
    encoded_arr = ""
  for char in text:
    encoded_arr += strcode_reverse[char] + ","
  encoded_arr += "EOM_"
  if args.array_name:
    encoded_arr += "};"
  print(encoded_arr)


def decode(args):
  array = args.array
  # Extract the contents of the array, so that this will work regardless of whether "static const
  # u16"... is included.
  try:
    array_contents = re.search("{(.+)}", array).group(1)
  except AttributeError:
    array_contents = array
  encoded_str = re.split(",", array_contents.strip())
  decoded_str = ""
  for char in encoded_str:
    if char != "EOM_":
      decoded_str += strcode[char]
  print(decoded_str)


def main():
  class MyParser(argparse.ArgumentParser):
    def error(self, message):
      sys.stderr.write('error: %s\n' % message)
      self.print_help()
      sys.exit(2)

  parser = MyParser(description="Converts text to and from the strcode format, used for debug \
menus.")
  subparsers = parser.add_subparsers()

  subparser_encode = subparsers.add_parser(
      "encode", help="Encodes text to strcode format.")
  subparser_encode.add_argument("text", help="Text to encode.", type=str)
  subparser_encode.add_argument("array_name", help="Name of the array.", type=str, nargs="?")
  subparser_encode.set_defaults(func=encode)

  subparser_decode = subparsers.add_parser(
      "decode", help="Decodes a message from strcode format.")
  subparser_decode.add_argument("array", help="Array to decode.", type=str)
  subparser_decode.set_defaults(func=decode)

  args = parser.parse_args()
  args.func(args)


if __name__ == "__main__":
  main()
