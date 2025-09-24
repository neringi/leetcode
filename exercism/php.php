<!DOCTYPE html>
<html>
    <head>
        <title>PHP Practice</title>
    </head>
    <body>
        <?php echo '<p>Exercism Practice</p>'; ?>
        <!-- Reverse a string -->
        <?php $a='stressed';
        $b = strrev($a);
        echo "Reversed string {$a} to: {$b}";
        ?>
        <!-- resistor color lookup (arrays) -->
        <?php
            function getAllColors(): array
            {
                return ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"];
            };
            function colorCode(string $color): int
            {
                return array_search($color, getAllColors());
            };
        ?>
        
    </body>
</html>