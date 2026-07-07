const fs = require('node:fs/promises');
const path = require('node:path');
const sharp = require('sharp');

const root = path.resolve(__dirname, '..');

const items = [
  {
    slide_number: 4,
    product: 'fifa',
    url: 'https://www.fifa.com/en',
    name: 'fifa_home_desktop',
    raw_path: 'assets/presentation/raw/fifa/fifa_home_desktop.png',
    annotated_path: 'assets/presentation/annotated/fifa/fifa_home_desktop.png',
    crop_path: 'assets/presentation/crops/fifa/fifa_home_desktop_crop.png',
    regions: [
      { label: 'A', text: 'Điều hướng toàn cục', x: 80, y: 4, width: 1280, height: 100 },
      { label: 'B', text: 'Lối vào World Cup', x: 80, y: 190, width: 1280, height: 104 },
    ],
    crop: { left: 60, top: 0, width: 1320, height: 840 },
    highlighted_element: 'Global navigation and official World Cup entry',
    hci_claim: 'FIFA.com supports broad information discovery through official task entry points.',
    caption: 'Trang chủ FIFA.com sạch: thanh điều hướng và lối vào World Cup đều nhìn thấy ngay.',
  },
  {
    slide_number: 6,
    product: 'fifa',
    url: 'https://www.fifa.com/en',
    name: 'fifa_home_mobile',
    raw_path: 'assets/presentation/raw/fifa/fifa_home_mobile.png',
    annotated_path: 'assets/presentation/annotated/fifa/fifa_home_mobile.png',
    crop_path: 'assets/presentation/crops/fifa/fifa_home_mobile_crop.png',
    regions: [
      { label: 'A', text: 'Điều hướng mobile', x: 2, y: 2, width: 386, height: 62 },
      { label: 'B', text: 'Tác vụ ưu tiên', x: 16, y: 88, width: 358, height: 154 },
    ],
    crop: { left: 0, top: 0, width: 390, height: 620 },
    highlighted_element: 'Mobile navigation and primary World Cup task',
    hci_claim: 'Users with limited attention need a visible primary destination and compact navigation.',
    caption: 'Mobile FIFA.com sau khi đóng popup: điều hướng và tác vụ chính không còn bị che.',
  },
  {
    slide_number: 8,
    product: 'fifa',
    url: 'https://www.fifa.com/en/match-centre',
    name: 'fifa_match_centre_desktop',
    raw_path: 'assets/presentation/raw/fifa/fifa_match_centre_desktop.png',
    annotated_path: 'assets/presentation/annotated/fifa/fifa_match_centre_desktop.png',
    crop_path: 'assets/presentation/crops/fifa/fifa_match_centre_desktop_crop.png',
    regions: [
      { label: 'A', text: 'Tìm kiếm và ngày', x: 80, y: 225, width: 1280, height: 145 },
      { label: 'B', text: 'Trạng thái trận', x: 80, y: 455, width: 955, height: 200 },
    ],
    crop: { left: 60, top: 130, width: 1320, height: 620 },
    highlighted_element: 'Search/date controls and match status list',
    hci_claim: 'Match Centre should reduce the path from competition intent to current match status.',
    caption: 'Match Centre desktop: bộ lọc ở trên, trạng thái trận ở ngay bên dưới.',
  },
  {
    slide_number: 8,
    product: 'fifa',
    url: 'https://www.fifa.com/en/match-centre',
    name: 'fifa_match_centre_mobile',
    raw_path: 'assets/presentation/raw/fifa/fifa_match_centre_mobile.png',
    annotated_path: 'assets/presentation/annotated/fifa/fifa_match_centre_mobile.png',
    crop_path: 'assets/presentation/crops/fifa/fifa_match_centre_mobile_crop.png',
    regions: [
      { label: 'A', text: 'Tìm giải đấu', x: 16, y: 208, width: 358, height: 44 },
      { label: 'B', text: 'Kết quả hiện tại', x: 16, y: 348, width: 358, height: 188 },
    ],
    crop: { left: 0, top: 90, width: 390, height: 650 },
    highlighted_element: 'Mobile search and current results',
    hci_claim: 'Mobile controls and results need strong hierarchy under limited screen space.',
    caption: 'Match Centre mobile: tìm kiếm và kết quả vẫn giữ thứ bậc rõ.',
  },
  {
    slide_number: 9,
    product: 'fifa',
    url: 'https://www.fifa.com/en/articles/mexico-england-match-report-highlights',
    name: 'fifa_article_desktop',
    raw_path: 'assets/presentation/raw/fifa/fifa_article_desktop.png',
    annotated_path: 'assets/presentation/annotated/fifa/fifa_article_desktop.png',
    crop_path: 'assets/presentation/crops/fifa/fifa_article_desktop_crop.png',
    regions: [
      { label: 'A', text: 'Ngữ cảnh giải đấu', x: 64, y: 40, width: 1280, height: 64 },
      { label: 'B', text: 'Tiêu đề bài viết', x: 190, y: 700, width: 1060, height: 230 },
    ],
    crop: { left: 170, top: 90, width: 1100, height: 880 },
    highlighted_element: 'Tournament context and article headline',
    hci_claim: 'The article preserves official tournament context while presenting a clear reading entry point.',
    caption: 'Bài viết FIFA thật: ngữ cảnh giải đấu và tiêu đề bài viết xuất hiện trong cùng màn hình.',
  },
  {
    slide_number: 9,
    product: 'fifa',
    url: 'https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026',
    name: 'fifa_tournament_desktop',
    raw_path: 'assets/presentation/raw/fifa/fifa_tournament_desktop.png',
    annotated_path: 'assets/presentation/annotated/fifa/fifa_tournament_desktop.png',
    crop_path: 'assets/presentation/crops/fifa/fifa_tournament_desktop_crop.png',
    regions: [
      { label: 'A', text: 'Điều hướng giải đấu', x: 64, y: 40, width: 1280, height: 64 },
      { label: 'B', text: 'Nội dung spotlight', x: 80, y: 360, width: 1280, height: 610 },
    ],
    crop: { left: 60, top: 40, width: 1320, height: 920 },
    highlighted_element: 'Tournament navigation and spotlight content',
    hci_claim: 'Tournament pages shift from global discovery to event-specific navigation and content.',
    caption: 'Trang giải đấu thật: điều hướng theo giải và nội dung spotlight được hiển thị rõ.',
  },
  {
    slide_number: 18,
    product: 'chess',
    url: 'https://www.chess.com/',
    name: 'chess_home_desktop',
    raw_path: 'assets/presentation/raw/chess/chess_home_desktop.png',
    annotated_path: 'assets/presentation/annotated/chess/chess_home_desktop.png',
    crop_path: 'assets/presentation/crops/chess/chess_home_desktop_crop.png',
    regions: [
      { label: 'A', text: 'Mô hình bàn cờ', x: 262, y: 16, width: 545, height: 545 },
      { label: 'B', text: 'CTA bắt đầu', x: 877, y: 350, width: 400, height: 75 },
    ],
    crop: { left: 170, top: 0, width: 1100, height: 860 },
    highlighted_element: 'Chessboard metaphor and Get Started CTA',
    hci_claim: 'The home page promotes immediate action but can expose too much complexity to first-time users.',
    caption: 'Trang chủ Chess.com: bàn cờ quen thuộc và CTA bắt đầu là hai điểm neo chính.',
  },
  {
    slide_number: 7,
    product: 'chess',
    url: 'https://www.chess.com/',
    name: 'chess_home_mobile',
    raw_path: 'assets/presentation/raw/chess/chess_home_mobile.png',
    annotated_path: 'assets/presentation/annotated/chess/chess_home_mobile.png',
    crop_path: 'assets/presentation/crops/chess/chess_home_mobile_crop.png',
    regions: [
      { label: 'A', text: 'Bàn cờ', x: 39, y: 49, width: 312, height: 312 },
      { label: 'B', text: 'Get Started', x: 39, y: 524, width: 312, height: 65 },
    ],
    crop: { left: 0, top: 0, width: 390, height: 700 },
    highlighted_element: 'Mobile board and primary CTA',
    hci_claim: 'A novice-facing mobile entry should keep the first action visible and understandable.',
    caption: 'Chess.com mobile: board và CTA chính vẫn đọc được trong một khung nhìn.',
  },
  {
    slide_number: 10,
    product: 'chess',
    url: 'https://www.chess.com/play/online',
    name: 'chess_play_desktop',
    raw_path: 'assets/presentation/raw/chess/chess_play_desktop.png',
    annotated_path: 'assets/presentation/annotated/chess/chess_play_desktop.png',
    crop_path: 'assets/presentation/crops/chess/chess_play_desktop_crop.png',
    regions: [
      { label: 'A', text: 'Bàn chơi', x: 228, y: 65, width: 688, height: 688 },
      { label: 'B', text: 'Thiết lập ván', x: 986, y: 96, width: 223, height: 330 },
    ],
    crop: { left: 170, top: 0, width: 1080, height: 900 },
    highlighted_element: 'Play board and game setup controls',
    hci_claim: 'Players can start a game quickly when the board and setup controls are visually separated.',
    caption: 'Play page công khai: bàn chơi và các lựa chọn bắt đầu ván nằm cạnh nhau.',
  },
  {
    slide_number: 14,
    product: 'chess',
    url: 'https://www.chess.com/puzzles',
    name: 'chess_puzzles_clean_desktop',
    raw_path: 'assets/presentation/raw/chess/chess_puzzles_clean_desktop.png',
    annotated_path: 'assets/presentation/annotated/chess/chess_puzzles_clean_desktop.png',
    crop_path: 'assets/presentation/crops/chess/chess_puzzles_clean_desktop_crop.png',
    regions: [
      { label: 'A', text: 'Bàn puzzle', x: 188, y: 16, width: 728, height: 728 },
      { label: 'B', text: 'Tiến trình + hành động', x: 947, y: 16, width: 300, height: 969 },
    ],
    crop: { left: 170, top: 0, width: 1080, height: 1000 },
    highlighted_element: 'Puzzle board and progression/action rail',
    hci_claim: 'Puzzle feedback combines direct manipulation with an explicit next action.',
    caption: 'Puzzle page sau khi đóng modal: bàn cờ và tiến trình hành động cùng hiển thị.',
  },
  {
    slide_number: 11,
    product: 'chess',
    url: 'https://www.chess.com/lessons',
    name: 'chess_lessons_clean_desktop',
    raw_path: 'assets/presentation/raw/chess/chess_lessons_clean_desktop.png',
    annotated_path: 'assets/presentation/annotated/chess/chess_lessons_clean_desktop.png',
    crop_path: 'assets/presentation/crops/chess/chess_lessons_clean_desktop_crop.png',
    regions: [
      { label: 'A', text: 'Nhóm nội dung học', x: 272, y: 190, width: 728, height: 116 },
      { label: 'B', text: 'Lộ trình người mới', x: 272, y: 438, width: 728, height: 230 },
    ],
    crop: { left: 170, top: 80, width: 1080, height: 820 },
    highlighted_element: 'Lesson categories and beginner learning path',
    hci_claim: 'Clear categories and a visible beginner path support progressive disclosure.',
    caption: 'Lessons page sau khi đóng modal: nhóm nội dung và lộ trình Learn To Play đều rõ.',
  },
];

function escapeXml(value) {
  return String(value)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;');
}

function overlaySvg(width, height, regions) {
  const mobile = width < 600;
  const stroke = mobile ? 3 : 5;
  const fontSize = mobile ? 12 : 20;
  const labelHeight = mobile ? 22 : 32;
  const parts = regions.map((region) => {
    const labelY = Math.max(0, region.y - labelHeight);
    const textWidth = Math.min(width - region.x - 4, Math.max(100, region.text.length * fontSize * 0.58 + 54));
    return `
      <rect x="${region.x}" y="${region.y}" width="${region.width}" height="${region.height}" fill="none" stroke="#ff2d20" stroke-width="${stroke}"/>
      <rect x="${region.x}" y="${labelY}" width="${textWidth}" height="${labelHeight}" fill="#ff2d20"/>
      <text x="${region.x + 8}" y="${labelY + labelHeight - (mobile ? 6 : 8)}" font-family="Arial" font-size="${fontSize}" font-weight="700" fill="#ffffff">${escapeXml(region.label)} · ${escapeXml(region.text)}</text>`;
  }).join('');
  return Buffer.from(`<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}">${parts}</svg>`);
}

async function annotate(item) {
  const raw = path.join(root, item.raw_path);
  const annotated = path.join(root, item.annotated_path);
  const cropPath = path.join(root, item.crop_path);
  await fs.mkdir(path.dirname(annotated), { recursive: true });
  await fs.mkdir(path.dirname(cropPath), { recursive: true });

  const metadata = await sharp(raw).metadata();
  const width = metadata.width;
  const height = metadata.height;
  if (!width || !height) throw new Error(`Missing dimensions: ${item.raw_path}`);

  for (const region of item.regions) {
    if (region.x < 0 || region.y < 0 || region.x + region.width > width || region.y + region.height > height) {
      throw new Error(`Region outside image: ${item.name} ${region.label}`);
    }
  }

  await sharp(raw)
    .composite([{ input: overlaySvg(width, height, item.regions), top: 0, left: 0 }])
    .png()
    .toFile(annotated);

  const crop = item.crop || { left: 0, top: 0, width, height };
  await sharp(annotated).extract(crop).png().toFile(cropPath);

  return {
    slide_number: item.slide_number,
    product: item.product,
    url: item.url,
    raw_path: item.raw_path,
    annotated_path: item.annotated_path,
    crop_path: item.crop_path,
    highlighted_element: item.highlighted_element,
    hci_claim: item.hci_claim,
    caption: item.caption,
    quality_status: 'verified',
  };
}

async function main() {
  const manifest = [];
  for (const item of items) manifest.push(await annotate(item));
  const manifestPath = path.join(root, 'assets/presentation/presentation_visual_manifest.json');
  await fs.writeFile(manifestPath, `${JSON.stringify({ generated_at: new Date().toISOString(), items: manifest }, null, 2)}\n`, 'utf8');
  console.log(JSON.stringify({ annotated: manifest.length, manifest: path.relative(root, manifestPath) }, null, 2));
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
