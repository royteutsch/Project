#############################################################################
# Generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#  Apr 19, 2022 11:05:50 AM +0300  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { 
    straightline_png "./straightLine.png" 
    curvedline_png "./curvedLine.png" 
    rectangle_png "./rectangle.png" 
    polyhedron_png "./polyhedron.png" 
    circle_png "./circle.png" 
    image28 "./painter.png" 
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
        -menu "$top.m46" -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 261x669+1389+238
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
    frame $top.fra48 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 617 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 142 
    vTcl:DefineAlias "$top.fra48" "FilterFrame" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra48
    label $site_3_0.lab56 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family David -size 20 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Filters 
    vTcl:DefineAlias "$site_3_0.lab56" "FilterLabel" vTcl:WidgetProc "Toplevel1" 1
    frame $site_3_0.fra57 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 115 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 145 
    vTcl:DefineAlias "$site_3_0.fra57" "TimeFilterFrame" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra57
    label $site_4_0.lab58 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font {-family David -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {From: } 
    vTcl:DefineAlias "$site_4_0.lab58" "FromLabel" vTcl:WidgetProc "Toplevel1" 1
    entry $site_4_0.ent59 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 64 
    vTcl:DefineAlias "$site_4_0.ent59" "FromEntry" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab60 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font {-family David -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text To: 
    vTcl:DefineAlias "$site_4_0.lab60" "ToLabel" vTcl:WidgetProc "Toplevel1" 1
    entry $site_4_0.ent61 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 64 
    vTcl:DefineAlias "$site_4_0.ent61" "ToEntry" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab62 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font {-family David -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Leave Empty for Present} 
    vTcl:DefineAlias "$site_4_0.lab62" "ExplanationLabel" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.lab58 \
        -in $site_4_0 -x 0 -relx 0.069 -y 0 -rely 0.087 -width 0 \
        -relwidth 0.372 -height 0 -relheight 0.27 -anchor nw \
        -bordermode ignore 
    place $site_4_0.ent59 \
        -in $site_4_0 -x 0 -relx 0.483 -y 0 -rely 0.087 -width 64 -relwidth 0 \
        -height 30 -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.lab60 \
        -in $site_4_0 -x 0 -relx 0.069 -y 0 -rely 0.348 -width 0 \
        -relwidth 0.303 -height 0 -relheight 0.27 -anchor nw \
        -bordermode ignore 
    place $site_4_0.ent61 \
        -in $site_4_0 -x 0 -relx 0.483 -y 0 -rely 0.348 -width 64 -relwidth 0 \
        -height 30 -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.lab62 \
        -in $site_4_0 -x 0 -relx 0.069 -y 0 -rely 0.696 -width 0 \
        -relwidth 0.855 -height 0 -relheight 0.27 -anchor nw \
        -bordermode ignore 
    frame $site_3_0.fra63 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 145 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 145 
    vTcl:DefineAlias "$site_3_0.fra63" "ColourFilterFrame" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra63
    label $site_4_0.lab64 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font {-family David -size 20 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Colour 
    vTcl:DefineAlias "$site_4_0.lab64" "ColourLabel" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_0.but65 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font {-family David -size 20 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Choose 
    vTcl:DefineAlias "$site_4_0.but65" "ColourButton" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.lab64 \
        -in $site_4_0 -x 0 -relx 0.207 -y 0 -rely 0.069 -width 0 \
        -relwidth 0.579 -height 0 -relheight 0.352 -anchor nw \
        -bordermode ignore 
    place $site_4_0.but65 \
        -in $site_4_0 -x 0 -relx 0.138 -y 0 -rely 0.552 -width 107 \
        -relwidth 0 -height 54 -relheight 0 -anchor nw -bordermode ignore 
    frame $site_3_0.fra66 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 165 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 145 
    vTcl:DefineAlias "$site_3_0.fra66" "UserFilterFrame" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra66
    label $site_4_0.lab67 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font {-family David -size 20 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Users 
    vTcl:DefineAlias "$site_4_0.lab67" "UserLabel" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_0.but68 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font {-family David -size 20 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Choose 
    vTcl:DefineAlias "$site_4_0.but68" "UserButton" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.lab67 \
        -in $site_4_0 -x 0 -relx 0.069 -y 0 -rely 0.061 -width 0 \
        -relwidth 0.855 -height 0 -relheight 0.37 -anchor nw \
        -bordermode ignore 
    place $site_4_0.but68 \
        -in $site_4_0 -x 0 -relx 0.138 -y 0 -rely 0.606 -width 107 \
        -relwidth 0 -height 54 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab56 \
        -in $site_3_0 -x 0 -relx 0.069 -y 0 -rely 0.02 -width 0 \
        -relwidth 0.855 -height 0 -relheight 0.16 -anchor nw \
        -bordermode ignore 
    place $site_3_0.fra57 \
        -in $site_3_0 -x 0 -y 0 -rely 0.178 -width 0 -relwidth 1 -height 0 \
        -relheight 0.228 -anchor nw -bordermode ignore 
    place $site_3_0.fra63 \
        -in $site_3_0 -x 0 -y 0 -rely 0.396 -width 0 -relwidth 1 -height 0 \
        -relheight 0.287 -anchor nw -bordermode ignore 
    place $site_3_0.fra66 \
        -in $site_3_0 -x 0 -y 0 -rely 0.673 -width 0 -relwidth 1 -height 0 \
        -relheight 0.327 -anchor nw -bordermode ignore 
    frame $top.fra49 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 448 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 84 
    vTcl:DefineAlias "$top.fra49" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra49
    button $site_3_0.but51 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -image straightline_png -pady 0 
    vTcl:DefineAlias "$site_3_0.but51" "StraightButton" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but52 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -image curvedline_png -pady 0 
    vTcl:DefineAlias "$site_3_0.but52" "CurvedButton" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but53 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -image rectangle_png -pady 0 
    vTcl:DefineAlias "$site_3_0.but53" "RectButton" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but54 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -image polyhedron_png -pady 0 
    vTcl:DefineAlias "$site_3_0.but54" "PolyButton" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but55 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -image circle_png -pady 0 
    vTcl:DefineAlias "$site_3_0.but55" "CircleButton" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.but51 \
        -in $site_3_0 -x 0 -y 0 -width 87 -relwidth 0 -height 94 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $site_3_0.but52 \
        -in $site_3_0 -x 0 -y 0 -rely 0.201 -width 87 -relwidth 0 -height 94 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but53 \
        -in $site_3_0 -x 0 -y 0 -rely 0.402 -width 87 -relwidth 0 -height 94 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but54 \
        -in $site_3_0 -x 0 -y 0 -rely 0.603 -width 87 -relwidth 0 -height 94 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but55 \
        -in $site_3_0 -x 0 -y 0 -rely 0.804 -width 87 -relwidth 0 -height 94 \
        -relheight 0 -anchor nw -bordermode ignore 
    button $top.but47 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -image image28 -pady 0 
    vTcl:DefineAlias "$top.but47" "ParamButton" vTcl:WidgetProc "Toplevel1" 1
    menu $top.m46 \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_menu_bg) \
        -font TkMenuFont -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra48 \
        -in $top -x 0 -relx 0.441 -y 0 -rely 0.015 -width 0 -relwidth 0.544 \
        -height 0 -relheight 0.951 -anchor nw -bordermode ignore 
    place $top.fra49 \
        -in $top -x 0 -relx 0.077 -y 0 -rely 0.136 -width 0 -relwidth 0.322 \
        -height 0 -relheight 0.67 -anchor nw -bordermode ignore 
    place $top.but47 \
        -in $top -x 0 -relx 0.077 -y 0 -rely 0.817 -width 89 -relwidth 0 \
        -height 94 -relheight 0 -anchor nw -bordermode ignore 
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

