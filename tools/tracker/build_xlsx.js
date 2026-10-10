/* GitHub runner Excel export; the canonical tracker is issues + data/*.json.
   The initial delivered workbook is generated with artifact_tool. In a standard
   GitHub runner this renderer uses portable ExcelJS, installed by the workflow.
*/
'use strict';
const fs = require('fs');
const path = require('path');
const ExcelJS = require('exceljs');
const ROOT = path.resolve(__dirname, '../..');
const tracking = path.join(ROOT, 'tracking');
const brand = JSON.parse(fs.readFileSync(path.join(ROOT,'config/brand.json'),'utf8'));
const features = JSON.parse(fs.readFileSync(path.join(ROOT,'data/features.json'),'utf8'));
const days = JSON.parse(fs.readFileSync(path.join(ROOT,'data/daily_plan.json'),'utf8'));

// Feature status is generated as CSV by the stdlib Python workflow.
const statusMap = {};
const csvPath = path.join(tracking,'Feature_Checklist.csv');
const dayCsvPath = path.join(tracking,'Daily_Checklist.csv');
// CSV parser supporting quoted commas, quotes and embedded newlines, not just split(',').
function parseCSV(s){
  s=s.replace(/^\uFEFF/,'');let rows=[],cur=[],cell='',quote=false;
  for(let i=0;i<s.length;i++){
    const c=s[i];
    if(quote){if(c==='"'){if(s[i+1]==='"'){cell+='"';i++;}else quote=false;}else cell+=c;}
    else if(c==='"')quote=true;
    else if(c===','){cur.push(cell);cell='';}
    else if(c==='\n'){cur.push(cell.replace(/\r$/,''));rows.push(cur);cur=[];cell='';}
    else cell+=c;
  }
  if(cell||cur.length){cur.push(cell);rows.push(cur);}
  return rows;
}
function readRecords(filepath){
  const rows=parseCSV(fs.readFileSync(filepath,'utf8'));
  const headers=rows.shift();
  return rows.filter(r=>r.length===headers.length).map(r=>Object.fromEntries(headers.map((h,i)=>[h,r[i]])));
}
const featureRecords=readRecords(csvPath);const dayRecords=readRecords(dayCsvPath);
const wb=new ExcelJS.Workbook();wb.creator=brand.display_name+' Progress Automation';
wb.created=new Date('2026-10-09T00:00:00Z');
const ink='18233B',teal='087F80',light='EAF7F5',soft='F0F4FA',muted='64748B';
function sheet(name,head,rows,widths){
  const ws=wb.addWorksheet(name,{views:[{state:'frozen',ySplit:4,xSplit:1}]});
  ws.mergeCells(1,1,1,head.length);
  ws.getCell(1,1).value=`${brand.display_name.toUpperCase()}  /  ${name.toUpperCase()}`;
  ws.getCell(1,1).fill={type:'pattern',pattern:'solid',fgColor:{argb:'FF'+ink}};
  ws.getCell(1,1).font={bold:true,color:{argb:'FFFFFFFF'},size:16};
  ws.getRow(1).height=35;
  ws.mergeCells(2,1,2,head.length);
  ws.getCell(2,1).value='Generated from verified GitHub Issues. Do not edit: changes will be replaced at the next sync.';
  ws.getCell(2,1).font={italic:true,color:{argb:'FF'+muted},size:10};
  ws.addRow([]);
  const hrow=ws.getRow(4);hrow.values=head;
  hrow.height=28;
  hrow.eachCell(cell=>{cell.fill={type:'pattern',pattern:'solid',fgColor:{argb:'FF'+teal}};
    cell.font={color:{argb:'FFFFFFFF'},bold:true};cell.alignment={vertical:'middle',wrapText:true};});
  for(const r of rows){let row=ws.addRow(r);row.height=31;
    row.alignment={vertical:'middle',wrapText:true};
    if(row.number%2===0)row.eachCell(c=>{c.fill={type:'pattern',pattern:'solid',fgColor:{argb:'FF'+soft}};});
    const check=row.getCell(1);check.font={bold:true,color:{argb:'FF'+(r[0]==='☑'?'087F80':'64748B')}};
  }
  head.forEach((_,i)=>ws.getColumn(i+1).width=widths[i]||18);
  ws.autoFilter={from:{row:4,column:1},to:{row:4+rows.length,column:head.length}};
  return ws;
}
const status=JSON.parse(fs.readFileSync(path.join(tracking,'status.json'),'utf8'));
const summary=wb.addWorksheet('Overview');summary.getColumn(1).width=34;summary.getColumn(2).width=18;
summary.mergeCells('A1:D1');summary.getCell('A1').value=`${brand.display_name} — BUILD PROGRESS`;
summary.getCell('A1').font={bold:true,size:18,color:{argb:'FFFFFFFF'}};
summary.getCell('A1').fill={type:'pattern',pattern:'solid',fgColor:{argb:'FF'+ink}};
summary.getRow(1).height=38;
summary.addRow(['Metric','Value']);
for(const [metric,value] of [
 ['Verified V1 features',`${status.v1_verified} / ${status.v1_total}`],
 ['V1 feature progress',status.v1_total?status.v1_verified/status.v1_total:0],
 ['Verified daily tasks',`${status.days_verified} / ${status.days_total}`],
 ['Last synchronized (UTC)',status.synced_at],
 ['Source','GitHub Issues + approved status labels']
]) summary.addRow([metric,value]);
summary.getCell('B4').numFmt='0.0%';
summary.getRow(2).font={bold:true};
summary.getCell('A10').value='Only closed issues with the verified label are checked. Closed alone is Needs Review.';
summary.mergeCells('A10:D10');summary.getCell('A10').font={color:{argb:'FF'+muted},italic:true};
const featSheet=sheet('Features',['Done','ID','Release','Category','Feature','Priority','Target Day','Status','Acceptance criteria','Owner','GitHub Issue'],
  featureRecords.map(r=>[r.Done,r.ID,r.Release,r.Category,r.Feature,r.Priority, r['Target Day']?Number(r['Target Day']):null,r.Status,r.Acceptance,r.Owner,r['GitHub Issue']]),
  [8,14,12,27,46,11,13,18,65,18,40]);
const dailySheet=sheet('Daily Plan',['Done','Day','ID','Week','Phase','Task','Status','Acceptance','Owner','GitHub Issue'],
  dayRecords.map(r=>[r.Done,Number(r.Day),r.ID,Number(r.Week),r.Phase,r.Task,r.Status,r.Acceptance,r.Owner,r['GitHub Issue']]),
  [8,9,14,9,27,65,18,48,15,38]);
// Instructions remain included each time the workbook is regenerated by GitHub Actions.
const howto=wb.addWorksheet('How To Use');
howto.getColumn(1).width=20;howto.getColumn(2).width=88;
howto.mergeCells('A1:B1');howto.getCell('A1').value='HOW AUTOMATIC CHECKMARKS WORK';
howto.getCell('A1').fill={type:'pattern',pattern:'solid',fgColor:{argb:'FF'+ink}};
howto.getCell('A1').font={bold:true,color:{argb:'FFFFFFFF'},size:16};howto.getRow(1).height=37;
const steps=[
  ['STEP 1','Create a private GitHub repo, push this starter pack and enable Issues and Actions.'],
  ['STEP 2','Create issues titled [FIN-001] ... or [DAY-001] ... using stable catalog IDs.'],
  ['STEP 3','Mark open issues in-progress or blocked when appropriate.'],
  ['STEP 4','Review the PR, passing tests, security/tax criteria and documentation.'],
  ['STEP 5','After independent verification, apply the verified label AND close the issue.'],
  ['STEP 6','GitHub Actions rebuilds the workbook, CSVs and progress documentation.'],
  ['STEP 7','A reopened verified issue is no longer checked.'],
  ['RENAME','Change config/brand.json or use scripts/rebrand.py; stable IDs persist.'],
  ['NOTE','The automation begins only after the GitHub repository is connected and enabled.']
];
steps.forEach((step,i)=>{const row=howto.getRow(i+3);row.values=step;row.height=36;
  row.getCell(1).fill={type:'pattern',pattern:'solid',fgColor:{argb:'FF'+light}};
  row.getCell(1).font={bold:true,color:{argb:'FF'+teal}};
  row.getCell(2).alignment={wrapText:true,vertical:'middle'};});

const out=path.join(tracking,'Project_Checklist.xlsx');
wb.xlsx.writeFile(out).then(()=>console.log('WROTE',out,featureRecords.length,dayRecords.length))
  .catch(e=>{console.error(e);process.exit(1);});
