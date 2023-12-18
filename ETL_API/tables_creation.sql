CREATE TABLE `tes_fastprint`.`kategori` ( `id_kategori` INT NULL AUTO_INCREMENT , `nama_kategori` VARCHAR(30) NULL , PRIMARY KEY (`id_kategori`)) ENGINE = InnoDB;

CREATE TABLE `tes_fastprint`.`status` ( `id_status` INT NULL AUTO_INCREMENT , `nama_status` VARCHAR(30) NULL , PRIMARY KEY (`id_status`)) ENGINE = InnoDB;

CREATE TABLE `tes_fastprint`.`produk` ( `id_produk` INT NULL AUTO_INCREMENT , `nama_produk` VARCHAR(120) NULL , `harga` INT UNSIGNED NULL , `kategori_id_fk` INT NULL , `status_id_fk` INT NULL , PRIMARY KEY (`id_produk`), INDEX `id_kategori` (`kategori_id_fk`), INDEX `id_status` (`status_id_fk`)) ENGINE = InnoDB;


ALTER TABLE `produk` ADD FOREIGN KEY (`kategori_id`) REFERENCES `kategori`(`id_kategori`) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE `produk` ADD FOREIGN KEY (`status_id`) REFERENCES `status`(`id_status`) ON DELETE RESTRICT ON UPDATE RESTRICT;

-- CARA LAIN DAPAT LANGSUNG MEMBUAT MODEL DJANGO DAN MELAKUKAN MIGRATION