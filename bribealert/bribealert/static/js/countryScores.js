(function($){

	var scorePhrases = [
		['gcb', '% of people have paid a bribe in the past 12 months.'],
		['increase', '% of people think that corruption has increased in the past 3 years.']
		['stayed', '% of people think that corruption stayed on the same level in the past 3 years.'],
		['decrease', '% of people think that corruption has decreased in the past 3 years.'],
		['ineffective', '% of people think that the government is ineffective in the fight against corruption.'],
		['neither_effective', '% of people think that the government is neither effective nor ineffective in the fight against corruption.'],
		['effective', '% of people think that the government is ineffective in the fight against corruption.'],
		['can_make_change', '% of people think that ordinary people can make a difference.'],
		['support', '% of people would support a colleague or friend.'],
		['involve', '% of people could imagin getting involved.'],
		['report', '% of people would report an incident.'],
		['politic', ''],
		['parliament', ''],
		['police', ''],
		['business', ''],
		['media', ''],
		['officials', ''],
		['judiciacy', ''],
		['ngo', ''],
		['religion', ''],
		['military', ''],
		['education', ''],
		['speed', ''],
		['problem', ''],
		['service', '']
	];
	
	$.fn.countryScores = function(){
		this.each(function(){
			var this.data("countryCode");

			var self = this;
			$.getJson('js/countryScores.json', function(data){
				phraseId = parseInt(Math.random()*scorePhrases.length -1);
				phrase = scorePhrases[phraseId];
				self.append(data[phrase[0]] + phrase[1]);
			});

			};
	};

	$(function(){
		$('p[data-countryCode]').countryScores();
	});

})(jQuery);