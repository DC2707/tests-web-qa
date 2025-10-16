<?php

function listarTests($dir) {
    $archivos = new RecursiveIteratorIterator(
        new RecursiveDirectoryIterator($dir)
    );

    $tests = [];
    foreach ($archivos as $archivo) {
        if ($archivo->isFile()) {
            $ruta = $archivo->getPathname();
            $ext = pathinfo($ruta, PATHINFO_EXTENSION);
            if (in_array($ext, ['py', 'js'])) {
                $tests[] = $ruta;
            }
        }
    }
    return $tests;
}

$baseDir = __DIR__;
$tests = listarTests($baseDir);


if (isset($_GET['file'])) {
    $file = realpath($_GET['file']);
    if (strpos($file, $baseDir) === 0 && file_exists($file)) {
        highlight_file($file);
        exit;
    } else {
        echo "<p><strong>Archivo no encontrado o acceso denegado.</strong></p>";
        exit;
    }
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Listado de Tests - Proyecto QA</title>
<style>
    body { font-family: Arial, sans-serif; background: #f4f4f4; color: #333; }
    h1 { background: #007acc; color: white; padding: 10px; border-radius: 8px; }
    table { border-collapse: collapse; width: 100%; background: white; }
    th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
    tr:hover { background: #eef; }
    a { text-decoration: none; color: #007acc; font-weight: bold; }
    .footer { margin-top: 20px; font-size: 12px; color: #777; text-align: center; }
</style>
</head>
<body>

<h1> Listado de Tests del Proyecto</h1>

<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Archivo</th>
            <th>Tipo</th>
            <th>Tamaño</th>
            <th>Ver</th>
        </tr>
    </thead>
    <tbody>
    <?php foreach ($tests as $i => $ruta): ?>
        <tr>
            <td><?= $i + 1 ?></td>
            <td><?= htmlspecialchars(str_replace($baseDir . DIRECTORY_SEPARATOR, '', $ruta)) ?></td>
            <td><?= strtoupper(pathinfo($ruta, PATHINFO_EXTENSION)) ?></td>
            <td><?= round(filesize($ruta) / 1024, 2) ?> KB</td>
            <td><a href="?file=<?= urlencode($ruta) ?>">Ver código</a></td>
        </tr>
    <?php endforeach; ?>
    </tbody>
</table>

<p class="footer">
Proyecto: <strong>tests-web-CI</strong> — Generado automáticamente el <?= date('d/m/Y H:i:s') ?>
</p>

</body>
</html>
