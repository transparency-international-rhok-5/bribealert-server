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
		['politic', '% of people see politics corrupt or extremely corrupt.'],
		['parliament', '% of people see parliament corrupt or extremely corrupt.'],
		['police', '% of people see police corrupt or extremely corrupt.'],
		['business', '% of people see business corrupt or extremely corrupt.'],
		['media', '% of people see media corrupt or extremely corrupt.'],
		['officials', '% of people see officials corrupt or extremely corrupt.'],
		['judiciary', '% of people see judiciary corrupt or extremely corrupt.'],
		['ngo', '% of people see NGOs corrupt or extremely corrupt.'],
		['religion', '% of people see religious bodies corrupt or extremely corrupt.'],
		['military', '% of people see military corrupt or extremely corrupt.'],
		['education', '% of people see the education system corrupt or extremely corrupt.'],
		['speed', '% of people payed their last bribe to speed things up.'],
		['problem', '% of people payed their last bribe to avoid problems with authorities.'],
		['service', '% of people payed their last bribe to receive a service entitled to it.']
	];
	
	$.fn.countryScores = function(){
		this.each(function(i, el){
			var self = $(el);
			var countryCode = self.data("countrycode");

			$.getJSON('js/countryScores.json', function(data){
				console.log(countryCode, data[countryCode]);
				phraseId = parseInt(Math.random()*(scorePhrases.length -1));
				phrase = scorePhrases[phraseId];
				if(!data[countryCode][phrase[0]] || !phrase[1]){
					self.append("there were no statistical relevant data collected yet.");
					return;
				};
				self.append(data[countryCode][phrase[0]] + phrase[1]);
			});

		});
	};

	$(function(){
		$('p[data-countryCode]').countryScores();
	});

})(jQuery);