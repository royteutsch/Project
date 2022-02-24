#############################################################################
# Generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#  Feb 24, 2022 10:40:33 AM +0200  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { 
}
vTcl:create_project_images $image_list   ;# In image.tcl

if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top1 {base} {
    global vTcl
    if {$base == ""} {
        set base .top1
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) 
    wm focusmodel $top passive
    wm geometry $top 494x196+699+314
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm deiconify $top
    set toptitle "Toplevel 0"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    frame $top.fra46 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 75 -width 245 
    vTcl:DefineAlias "$top.fra46" "ColourPreviewFrame" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra46
    label $site_3_0.lab47 \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font {-family David -size 24 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -text L: 
    vTcl:DefineAlias "$site_3_0.lab47" "LinePreviewLabel" vTcl:WidgetProc "Toplevel1" 1
    canvas $site_3_0.can48 \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -closeenough 1.0 \
        -height 53 -insertbackground black -relief ridge \
        -selectbackground blue -selectforeground white -width 53 
    vTcl:DefineAlias "$site_3_0.can48" "LineColourPreview" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab49 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font {-family David -size 24 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text F: 
    vTcl:DefineAlias "$site_3_0.lab49" "FillPreviewLabel" vTcl:WidgetProc "Toplevel1" 1
    canvas $site_3_0.can50 \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -closeenough 1.0 \
        -height 53 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -insertbackground black -relief ridge \
        -selectbackground blue -selectforeground white -width 53 
    vTcl:DefineAlias "$site_3_0.can50" "FillColourPreview" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab47 \
        -in $site_3_0 -x 0 -relx 0.041 -y 0 -rely 0.133 -width 0 \
        -relwidth 0.139 -height 0 -relheight 0.68 -anchor nw \
        -bordermode ignore 
    place $site_3_0.can48 \
        -in $site_3_0 -x 0 -relx 0.204 -y 0 -rely 0.133 -width 0 \
        -relwidth 0.216 -height 0 -relheight 0.707 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab49 \
        -in $site_3_0 -x 0 -relx 0.49 -y 0 -rely 0.133 -width 0 \
        -relwidth 0.139 -height 0 -relheight 0.68 -anchor nw \
        -bordermode ignore 
    place $site_3_0.can50 \
        -in $site_3_0 -x 0 -relx 0.653 -y 0 -rely 0.133 -width 0 \
        -relwidth 0.216 -height 0 -relheight 0.707 -anchor nw \
        -bordermode ignore 
    frame $top.fra51 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 75 -width 255 
    vTcl:DefineAlias "$top.fra51" "LineWidthSelectionFrame" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra51
    label $site_3_0.lab52 \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font {-family David -size 24 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -text {Line Width:} 
    vTcl:DefineAlias "$site_3_0.lab52" "LineWidthLabel" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent53 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 44 
    vTcl:DefineAlias "$site_3_0.ent53" "LineWidthEntry" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab52 \
        -in $site_3_0 -x 0 -relx 0.078 -y 0 -rely 0.133 -width 0 \
        -relwidth 0.643 -height 0 -relheight 0.68 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent53 \
        -in $site_3_0 -x 0 -relx 0.784 -y 0 -rely 0.133 -width 44 -relwidth 0 \
        -height 50 -relheight 0 -anchor nw -bordermode ignore 
    label $top.lab54 \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font {-family David -size 24 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -text {L: (     ,      ,      )} 
    vTcl:DefineAlias "$top.lab54" "LineColourSelectionLabel" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent55 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 34 
    vTcl:DefineAlias "$top.ent55" "LineRValueEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent56 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 34 
    vTcl:DefineAlias "$top.ent56" "LineGValueEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent57 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 34 
    vTcl:DefineAlias "$top.ent57" "LineBValueEntry" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab58 \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font {-family David -size 24 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -text {F: (     ,     ,      )} 
    vTcl:DefineAlias "$top.lab58" "FillColourSelectionLabel" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent59 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 34 
    vTcl:DefineAlias "$top.ent59" "FillRValueEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent60 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 34 
    vTcl:DefineAlias "$top.ent60" "FillGValueEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent61 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 34 
    vTcl:DefineAlias "$top.ent61" "FillBValueEntry" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra46 \
        -in $top -x 0 -y 0 -width 0 -relwidth 0.496 -height 0 \
        -relheight 0.383 -anchor nw -bordermode ignore 
    place $top.fra51 \
        -in $top -x 0 -relx 0.486 -y 0 -width 0 -relwidth 0.516 -height 0 \
        -relheight 0.383 -anchor nw -bordermode ignore 
    place $top.lab54 \
        -in $top -x 0 -relx 0.02 -y 0 -rely 0.459 -width 0 -relwidth 0.453 \
        -height 0 -relheight 0.311 -anchor nw -bordermode ignore 
    place $top.ent55 \
        -in $top -x 0 -relx 0.121 -y 0 -rely 0.51 -width 34 -relwidth 0 \
        -height 40 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent56 \
        -in $top -x 0 -relx 0.223 -y 0 -rely 0.51 -width 34 -relwidth 0 \
        -height 40 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent57 \
        -in $top -x 0 -relx 0.324 -y 0 -rely 0.51 -width 34 -relwidth 0 \
        -height 40 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab58 \
        -in $top -x 0 -relx 0.506 -y 0 -rely 0.459 -width 0 -relwidth 0.453 \
        -height 0 -relheight 0.311 -anchor nw -bordermode ignore 
    place $top.ent59 \
        -in $top -x 0 -relx 0.607 -y 0 -rely 0.51 -width 34 -relwidth 0 \
        -height 40 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent60 \
        -in $top -x 0 -relx 0.688 -y 0 -rely 0.51 -width 34 -relwidth 0 \
        -height 40 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent61 \
        -in $top -x 0 -relx 0.789 -y 0 -rely 0.51 -width 34 -relwidth 0 \
        -height 40 -relheight 0 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top1 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}

