/********************************************
 * REVOLUTION 5.2.5.1 EXTENSION - VIDEO FUNCTIONS
 * @version: 2.0.1 (18.10.2016)
 * @requires jquery.themepunch.revolution.js
 * @author ThemePunch
*********************************************/
(function($) {
	"use strict";
var _R = jQuery.fn.revolution,
	_ISM = _R.is_mobile(),
	extension = {	alias:"Video Min JS",
					name:"revolution.extensions.video.min.js",
					min_core: "5.3",
					version:"2.0.1"
			  };



///////////////////////////////////////////
// 	EXTENDED FUNCTIONS AVAILABLE GLOBAL  //
///////////////////////////////////////////
jQuery.extend(true,_R, {

	
	preLoadAudio : function(li,opt) {
		if (_R.compare_version(extension).check==="stop") return false;
		li.find('.tp-audiolayer').each(function() {

			var element = jQuery(this),
				obj = {};
			if (element.find('audio').length===0) {
				obj.src =  element.data('videomp4') !=undefined ? element.data('videomp4')  : '',
				obj.pre = element.data('videopreload') || '';
				if (element.attr('id')===undefined) element.attr('audio-layer-'+Math.round(Math.random()*199999));
				obj.id = element.attr('id');
				obj.status = "prepared";
				obj.start = jQuery.now();
				obj.waittime = element.data('videopreloadwait')*1000 || 5000;


				if (obj.pre=="auto" || obj.pre=="canplaythrough" || obj