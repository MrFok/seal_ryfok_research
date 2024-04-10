output = extractTemplates(["com.package.java.oneApple", "com.package.java.oneBanana", "com.package.java.oneCarrot", "com.package.java.twoCarrot", "com.package.java.threeCarrot"]);
// output = generateWildcardPatterns("com.package.java.oneApple");
console.log(output);


/**
 * Extracts all possible templates from an array of strings.
 *
 */
function extractTemplates(strings) {

    let splitStrings = strings.map(s => s.split(/(?=[A-Z])|\b/));
    var allTemplates = [];
    // let clusters = clusterStrings(splitStrings, 2);
    // var templates = clusters.map(cluster => findTemplate(cluster));
    // console.log(templates);
    for (let i = 2; i <= 5; i++) {
        let clusters = clusterStrings(splitStrings, i);

        var templates = clusters.map(cluster => findTemplate(cluster));

        allTemplates.push(templates);
    }

    return allTemplates;
}

function findTemplate(strings) {
    let template = strings[0].map((_, i) => strings.every(s => s[i] === strings[0][i]) ? strings[0][i] : '\\w+');
    return template.join(' ');
}

function calculateSimilarity(str1, str2) {
    let words1 = new Set(str1);
    let words2 = new Set(str2);
    let commonWords = new Set([...words1].filter(word => words2.has(word)));
    return commonWords.size;
}

function clusterStrings(strings, threshold ) {
    let clusters = [];
     

    strings.forEach(str => {
        let added = false;
        for (let cluster of clusters) {
            let similarity = calculateSimilarity(str, cluster[0]);
            if (similarity >= threshold) {
                cluster.push(str);
                added = true;
                break;
            }
        }
        if (!added) {
            clusters.push([str]);
        }
    });
    return clusters;
}

function generateWildcardPatterns(str) {
    let parts = str.split('.');
    let patterns = [];
    let pattern = '';

    for (let part of parts) {
        let subParts = part.split(/(?=[A-Z])/);
  
        for (let subPart of subParts) {
            pattern += subPart;
            patterns.push(pattern + '.*');
        }
  
        pattern += '.';
    }
  
    return patterns.filter((value, index, self) => self.indexOf(value) === index).slice(0, -1);
  }
